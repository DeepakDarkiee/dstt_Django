from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_admin',
            'is_employee',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
(None,{'classes': ('wide',),
        'fields': ('email', 'full_name','password1', 'password2')}),



('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_admin',
            'is_employee',
            'groups',
            'user_permissions',
        )}),
    )

    list_display = ('email', 'full_name' ,'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
# class CustomUserAdmin(UserAdmin):
#     list_filter = ('is_staff','is_admin','is_superuser','groups__name')
#     fieldsets =  (
#     (None, {'fields':('email','password')}),
#      ('Personal info', {'fields': ('full_name')}),
#      ('Permissions',{'fields':('is_staff','is_admin','is_active','is_superuser','user_permissions','groups')}),
#      )
#     add_fieldsets = (
#     (None, {'classes': ('extrapretty',), 'fields': ('email', 'password1', 'password2'),}),
#     (_('Personal info'), {'fields': ('full_name')}),
#     (_('Permissions'),{'fields':('is_staff','is_admin','is_active','is_superuser','groups','user_permissions')}),
#      )
#     list_display = ('email', 'name', 'is_staff', 'last_login')
#     search_fields =('email','full_name',)
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)

# admin.site.register(User,CustomUserAdmin)
