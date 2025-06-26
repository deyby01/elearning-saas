from django.contrib import admin
from .models import Tenant

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    """
    Configuración para el modelo Tenant en el panel de administración.
    """
    list_display = ('name', 'subdomain', 'owner', 'created_at')
    search_fields = ('name', 'subdomain', 'owner__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
