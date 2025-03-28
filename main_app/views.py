from django.shortcuts import render

from hard_python.main_app.models import Py_objects


def main_view(request):
    py_objects =Py_objects.objects.all()
    context = {
        'py_objects': py_objects
    }
    return render(request, 'main_app/main.html', context)
