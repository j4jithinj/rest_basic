from re import I
from django.urls import path 
from . import views
from .serializers import ProductSerializer
from .models import Product

urlpatterns = [ 
    path('product/create/list/', views.ProductView1.as_view(), name='product-list-create'),
    path('product/create/', views.ProductView2.as_view(), name='product-create'),
    path('product/list/', views.ProductView3.as_view(), name='product-list'),
    path('product/get/<str:pk>/', views.ProductView4.as_view(), name='product-get'),
    path('product/destroy/<str:pk>/', views.ProductView5.as_view(), name='product-destroy'),
    path('product/update/<str:pk>/', views.ProductView6.as_view(), name='product-update'),
    path('product/RetrieveUpdateDestroyAPIView/<str:pk>/', views.RetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('product/RetrieveUpdateAPIView/<str:pk>/', views.RetrieveUpdateAPIView.as_view(), name='product-retrieve-update'),
    path('product/RetrieveDestroyAPIView/<str:pk>/', views.RetrieveDestroyAPIView.as_view(), name='product-retrieve-destroy'),

    path('product/generic/', views.GenericView.as_view(), name='product-generic'),
    
    path('product/multiple/', views.TextAPIView.as_view(), name='product-multiple'),
    path('product/flat/', views.TextAPIFlatView.as_view(), name='product-multiple-flat'),

    path('product/CreateAPIView/', views.CreateAPIView.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer), name='user-list')
]