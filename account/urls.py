from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('signin/',views.SignInView.as_view(),name='signin'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('role/',views.RegisterRole.as_view(),name='role'),
    path('role_permission/',views.AddRolePermission.as_view(),name='role_permission'),
]