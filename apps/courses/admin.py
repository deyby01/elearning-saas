from django.contrib import admin
from .models import Course, Lesson

class LessonInline(admin.TabularInline):
    """
    Permite editar lecciones directamente desde la vista de edicion del Curso.
    """
    model = Lesson
    extra = 1 # Muestra un campo para una nueva leccion por defecto.
    ordering = ('order',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Configuración para el modelo Course en el panel de administración.
    """
    list_display = ('title', 'instructor', 'tenant', 'created_at')
    list_filter = ('tenant', 'instructor', 'created_at')
    search_fields = ('title', 'description', 'instructor__username', 'tenant__name')
    ordering = ('-created_at',)
    inlines = [LessonInline]  # ¡Aqui esta la magia!