from django.conf import settings
from django.db import models
from apps.tenants.models import Tenant

# Create your models here.
class Course(models.Model):
    """
    Representa un curso en la plataforma.
    Cada curso pertenece a una Escuela (Tenant) y es creado por un Instructor (User).
    """
    title = models.CharField(max_length=200, verbose_name='Titulo del Curso')
    description = models.TextField(verbose_name='Descripcion')
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, # Permitimos que el instructor sea nulo por si la cuenta es eliminada
        related_name='courses_taught',
        verbose_name='Instructor'
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Escuela'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Ultima Actualización')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-created_at'] 