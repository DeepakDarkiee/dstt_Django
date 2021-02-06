from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('signin/',views.SignInView.as_view(),name='signin'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('role/',views.RolesPermissions.as_view(),name='role'),
=======
    path('',views.SignInView.as_view(),name='signin'),
    path('logout/',views.LogoutView.as_view(),name='logout')
>>>>>>> 7abf9e4a360230e45adacca79b2f4098581ab58a
]