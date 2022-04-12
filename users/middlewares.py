import json

from rest_framework_simplejwt.backends import TokenBackend

from . import models
from . import configurations


class ActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.content_type in [
            "multipart/form-data",
            "application/x-www-form-urlencoded",
        ]:
            request_body = request.POST
        elif request.content_type in ["json", "application/json"]:
            request_body = json.loads(request.body.decode("utf-8"))
        else:
            request_body = {}
        response = self.get_response(request)

        if request.resolver_match is None or request.path_info.startswith("/admin/"):
            return response
        if request.resolver_match is None or request.path_info.startswith("/media/"):
            return response
        exceptional_urls = ("openapi-schema", "swagger", "redoc")
        if request.resolver_match.url_name in exceptional_urls:
            return response
        # No need to save activity if the request hit is not a successful
        if not str(response.status_code).startswith("2") or request.method == "OPTIONS":
            return response

        request_config = configurations.USER_ACTIONS.get(request.method, None)
        if request_config is None:
            raise ValueError(
                f"Please set the {request.method} (USER_ACTIONS) for the request in `users/configurations.py` file."
            )

        url_config = request_config.get(request.resolver_match.url_name, None)
        if url_config is None:
            raise ValueError(
                f"Please set the {request.resolver_match.url_name} (USER_ACTIONS) for the request in `users/configurations.py` file."
            )

        description = url_config.get("description", None)
        if description is None:
            raise ValueError(
                "Please set the description (USER_ACTIONS) for the request in `users/configurations.py` file."
            )
        user = request.user

        # Getting user for `login` and `refresh` (AnonymousUser)
        if request.resolver_match.url_name == "login":
            username = request_body.get("username", None)
            user = models.User.objects.filter(username=username).first()

        elif request.resolver_match.url_name == "refresh":
            refresh = request_body.get("refresh", None)
            valid_data = TokenBackend(
                algorithm="HS256").decode(refresh, verify=False)
            user_id = valid_data.get("user_id", None)
            user = models.User.objects.filter(id=user_id).first()

        if user is not None:
            models.Activity.objects.create(
                user=user, name=request.resolver_match.url_name, description=description
            )

        return response

    def process_view(request, view_func, view_args, view_kwargs): pass
    # This code is executed just before the view is called

    def process_exception(request, exception): pass
    # This code is executed if an exception is raised

    def process_template_response(request, response):
        # This code is executed if the response contains a render() method
        return response

# class ActivityMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         response = self.get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     def process_view(request, view_func, view_args, view_kwargs): pass
#     # This code is executed just before the view is called

#     def process_exception(request, exception): pass
#     # This code is executed if an exception is raised

#     def process_template_response(request, response):
#         # This code is executed if the response contains a render() method
#         return response
