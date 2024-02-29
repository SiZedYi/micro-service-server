from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import User,Product
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('user_id', 'user_name', 'name', 'email', 'is_staff')
    list_filter = ()
    ordering = ('user_id',)

    add_fieldsets = (
        (None, {'fields': ( 'last_login', 'name','user_name', 'password', 'email', 'is_manager', 'is_staff')}),
    )

admin.site.register(User)
admin.site.register(Product)



