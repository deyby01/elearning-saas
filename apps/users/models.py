from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Modelo de Usuario Personalizado.
    Hereda de AbstractUser, por lo que tenemos todos los campos de Django
    (username, email, password, etc.) y podemos añadir más en el futuro.
    """
    # Por ahora, no necesitamos añadir campos adicionales, pero el modelo ya está preparado.
    # Ejemplo de campo que podríamos añadir en el futuro:
    # email = models.EmailField(unique=True) # Para hacer el email el login principal y único
    
    pass