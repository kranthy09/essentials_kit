from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('forms/', views.FormList.as_view()),
    path('form/<int:pk>/', views.FormDetail.as_view()),
    path('items/', views.ItemList.as_view()),
    path('item/<int:pk>/', views.ItemDetail.as_view()),
    path('brands/', views.BrandList.as_view()),
    path('brand/<int:pk>/', views.BrandDetail.as_view()),
    path('itembrands/', views.ItemBrandList.as_view()),
    path('products/', views.ProductList.as_view()),
]