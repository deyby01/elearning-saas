from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Configuración para el modelo Course en el panel de administración.
    """
    list_display = ('title', 'instructor', 'tenant', 'created_at')
    list_filter = ('tenant', 'instructor', 'created_at')
    search_fields = ('title', 'description', 'instructor__username', 'tenant__name')
    ordering = ('-created_at',)