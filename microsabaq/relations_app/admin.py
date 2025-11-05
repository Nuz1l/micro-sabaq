from django.contrib import admin
from .models import Student, Group, Club
from django.contrib import admin
from django.contrib.admin import AdminSite

admin.site.site_header = "Панель управления Relations"
admin.site.site_title = "Relations Admin"
admin.site.index_title = "Добро пожаловать в админку"


from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage

class CustomAdminSite(admin.AdminSite):
    site_header = "Relations Панель"
    site_title = "Relations Admin"
    index_title = "Добро пожаловать"
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }

# Применить кастомный стиль к текущей админке
admin.site.site_header = CustomAdminSite.site_header
admin.site.site_title = CustomAdminSite.site_title
admin.site.index_title = CustomAdminSite.index_title



@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'curator')
    search_fields = ('name', 'curator')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'group_name')
    list_filter = ('group', 'clubs')
    search_fields = ('first_name', 'last_name')
    filter_horizontal = ('clubs',)

    def group_name(self, obj):
        return obj.group.name if obj.group else '-'
    group_name.short_description = 'Группа'
