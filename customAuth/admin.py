from django.contrib import admin

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
# TODO: Register more things after adding them to profile

class UserAdmin(UserAdmin):
	list_display = ('email', 'last_login', 'is_active', 'is_staff', 'is_superuser')
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	readonly_fields = ('username', 'email', 'date_joined', 'last_login')

	# def has_add_permission(self, request, obj=None):
	# 	return request.user.is_staff or (obj and obj.id == request.user.id)
	
	# def has_change_permission(self, request, obj=None):
	# 	return request.user.is_staff or (obj and obj.id == request.user.id)

	# def has_delete_permission(self, request, obj=None):
	# 	return request.user.is_staff or (obj and obj.id == request.user.id)

	# def has_module_permission(self, request):
	# 	return request.user.is_staff

	filter_horizontal = ()
	fieldsets = ()


admin.site.register(User, UserAdmin)