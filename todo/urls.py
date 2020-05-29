from django.urls import path
from .views import *
from django.views.decorators.http import require_POST
from .forms import TodoForm

urlpatterns = [
    path('fetch/', todo_fetch, name='fetch'),
    path('save/', todo_save, name='save'),
]

@csrf_exempt
@require_POST
def todo_save(request):
    if request.body:
        data = json.load(request.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()
    return JsonResponse({})


