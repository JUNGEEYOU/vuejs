from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
import json

def index(request):
    return render(request, 'todo/list.html')

def todo_fetch(request):
    """
    목록을 불러오는 역할
    :param request:
    :return:
    """
    todos = Todo.objects.all()
    todo_list =[]
    for index, todo in enumerate(todos, start=1):
        todo_list.append({'id':index, 'title': todo.title, 'completed': todo.completed})
    return JsonResponse(todo_list, safe=False)


def todo_save(request):
    """
    할일 목록 전체 데이터를 받아 그대로 저장 
    :param request:
    :return:
    """
    if request.body:
        data = json.load(request.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                print('todo', todo)
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()
    return JsonResponse({})
