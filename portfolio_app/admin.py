from django.contrib import admin
from .models import CustomUser, Experience, Project, Skill, Connection

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'home_address', 'location')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'home_address')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Connection)