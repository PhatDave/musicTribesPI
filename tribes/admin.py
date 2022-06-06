from django.contrib import admin
from .models import Tribe


# TODO: Added so I can manipulate
class TribeAdmin(admin.ModelAdmin):
	list_display = ('chieftain', 'name', 'logo', 'genre', 'created_at')
	search_fields = ('chieftain__username', 'name')
	readonly_fields = ('created_at',)

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
	list_filter = ()
	fieldsets = ()


admin.site.register(Tribe, TribeAdmin)