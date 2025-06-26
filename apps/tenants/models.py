from django.conf import settings
from django.db import models

# Create your models here.
class Tenant(models.Model):
    """
    Representa una escuela o inquilino en la plataforma.
    Cada tenant tiene su propio nombre, subdominio y dueño.
    """
    name = models.CharField(max_length=100, verbose_name='Nombre de la Escuela')
    subdomain = models.CharField(max_length=100, unique=True, verbose_name='Subdominio')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tenants',
        verbose_name='Dueño'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    
    def __str__(self):
        return f'{self.name} ({self.subdomain})'
    
    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'