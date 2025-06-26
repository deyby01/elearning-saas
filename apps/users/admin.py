from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Configuración personalizada para el modelo User en el panel de administración.
    Heredamos de UserAdmin para obtener toda su funcionalidad base
    y podemos extenderla aquí si es necesario.
    """
    # Por ahora, no necesitamos personalización extra, así que simplemente
    # heredamos y registramos. En el futuro, podríamos añadir campos
    # a list_display, crear filtros, etc.
    pass