from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses' # Nombre que usaremos en la plantilla