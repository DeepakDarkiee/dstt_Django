from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User
from django.utils.translation import ugettext_lazy as _

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','is_staff')
    list_filter = ('is_staff','is_admin','is_superuser','groups__name')
    fieldsets =  (
    (None, {'fields':('email','password')}),
     ('Personal info', {'fields': ('first_name', 'last_name')}),
     ('Permissions',{'fields':('is_staff','is_admin','is_active','is_superuser','user_permissions','groups')}),
     )
    add_fieldsets = (
    (None, {'classes': ('extrapretty',), 'fields': ('email', 'password1', 'password2'),}),
    (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    (_('Permissions'),{'fields':('is_staff','is_admin','is_active','is_superuser','groups','user_permissions')}),
     )
   
    search_fields =('email','first_name','last_name',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,CustomUserAdmin)
