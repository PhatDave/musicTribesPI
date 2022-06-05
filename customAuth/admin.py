from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'last_login', 'is_active', 'is_staff', 'is_superuser')
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	readonly_fields = ('username', 'email', 'date_joined', 'last_login')

	filter_horizontal = ()
	fieldsets = ()


admin.site.register(User, CustomUserAdmin)