from django.contrib import admin
from .models import User, UserTribeMember
from django.contrib.auth.admin import UserAdmin


# TODO: Added so I can manipulate
class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'last_login', 'is_active', 'is_staff', 'is_superuser')
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	readonly_fields = ('username', 'email', 'date_joined', 'last_login')

	filter_horizontal = ()
	fieldsets = ()


class CustomUserTribeMemberAdmin(admin.ModelAdmin):
	list_display = ('user', 'tribe')
	search_fields = ('user', 'tribe')
	list_filter = ()
	readonly_fields = ()

	def has_add_permission(self, request, obj=None):
		return request.user.is_superuser
	
	def has_change_permission(self, request, obj=None):
		return request.user.is_superuser
	
	def has_view_permission(self, request, obj=None):
		return request.user.is_superuser

	def has_delete_permission(self, request, obj=None):
		return request.user.is_superuser

	def has_module_permission(self, request):
		return request.user.is_superuser

	filter_horizontal = ()
	fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserTribeMember, CustomUserTribeMemberAdmin)
