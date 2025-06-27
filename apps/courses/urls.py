from django.urls import path
from . import views

app_name = 'courses' # Buena practica para nombrar las urls

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
]
