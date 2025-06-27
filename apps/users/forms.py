from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Puedes especificar los campos que quieres en el formulario
        fields = ('username', 'email', 'first_name', 'last_name')