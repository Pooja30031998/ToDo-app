from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ListForm
from .models import Todo

# Create your views here.
def createTodoListView(request):
    form = ListForm
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template = loader.get_template("todo.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))

def showTodoListView(request):
    obj = Todo.objects.all()
    template = loader.get_template("show.html")
    context = {"obj": obj}
    return HttpResponse(template.render(context, request))

def updateTodoListView(request, f_id):
    obj = Todo.objects.get(id=f_id)
    form = ListForm(instance=obj)
    if request.method == "POST":
        form = ListForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template = loader.get_template("todo.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))

def deleteTodoListView(request, f_id):
    obj = Todo.objects.get(id = f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    template = loader.get_template("confirmation.html")
    context = {"obj": obj}
    return HttpResponse(template.render(context, request))
