from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view()),
    path('forms/', views.FormList.as_view()),
    path('items/', views.ItemList.as_view()),
    path('brands/', views.BrandList.as_view()),
    path('itembrands/', views.ItemBrandList.as_view()),
]