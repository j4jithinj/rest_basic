from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from generics import mixins

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class Activity(mixins.GenericModelMixin):
#     class Action(models.TextChoices):
#         login = "login", "Login"
#         logout = "logout", "Logout"

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50,
#                             choices=Action.choices,
#                             default=Action.login)
#     description = models.TextField(blank=True, null=True)
#     arguments = models.JSONField(null=False, default=dict)
#     organization = models.ForeignKey(Organization,null=True,on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         verbose_name_plural = "Activities"