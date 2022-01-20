from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.order_by('group').prefetch_related('teachers')
    context = {
        'object_list': object_list,
        }
    return render(request, template, context)


# class StudentList(ListView):
#     model = Student
#     template = 'school/students_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_list'] = Student.objects.order_by('group').prefetch_related('teacher')
#         return context
#
#     def get_queryset(self):
#         return Student.objects.order_by('group').prefetch_related('teacher')