from re import I
from django.urls import path 
from . import views

urlpatterns = [ 
    path('product/create/list/', views.ProductView1.as_view(), name='product-list-create'),
    path('product/create/', views.ProductView2.as_view(), name='product-create'),
    path('product/list/', views.ProductView3.as_view(), name='product-list'),
    path('product/get/<str:pk>/', views.ProductView4.as_view(), name='product-get'),
    path('product/destroy/<str:pk>/', views.ProductView5.as_view(), name='product-destroy'),
    path('product/update/<str:pk>/', views.ProductView6.as_view(), name='product-update'),
]