from django.contrib import admin
from django.urls import path,include
from . import views

# urls
urlpatterns = [
    path('',views.SignInView.as_view(),name='signin'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('role/',views.RegisterRole.as_view(),name='role'),
    path('rolepermission/<str:name>',views.RolePermissionView.as_view(),name='rolepermission'),
    path('RemoveRole/<str:name>',views.RemoveRole.as_view(),name='RemoveRole'),
    

]
