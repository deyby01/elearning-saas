from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Vista de registro la que acabamos de crear
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    # Vistas de login y logout usando las de Django
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
