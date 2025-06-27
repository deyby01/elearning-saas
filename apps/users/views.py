from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # Usamos reverse_lazy para redirigir el usuario al login despues de un registro exitoso
    # 'login' es el nombre que le daremos a la URL de login en el siguiente paso.
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'