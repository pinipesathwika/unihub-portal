from django.contrib import admin

admin.site.site_header = "UniHub Admin"
admin.site.site_title = "UniHub Portal"
admin.site.index_title = "Welcome to UniHub Admin Panel"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Course, Assignment

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Assignment)
