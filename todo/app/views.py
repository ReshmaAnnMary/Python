from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TODO
from .forms import Form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.
class Listview(ListView):
    model = TODO
    template_name = 'index.html'
    context_object_name = 'data'


class Detailsview(DetailView):
    model = TODO
    template_name = 'details.html'
    context_object_name = 'task'


class Editview(UpdateView):
    model = TODO
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('app:details', kwargs={'pk': self.object.id})


class Delete(DeleteView):
    model = TODO
    template_name = 'delete.html'
    success_url = reverse_lazy('app:cbvhome')


def index(request):
    value = TODO.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = TODO(task=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'data': value})


def delete(request, id):
    value = TODO.objects.get(id=id)
    if request.method == 'POST':
        value.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    id = TODO.objects.get(id=id)
    form_data = Form(request.POST or None, instance=id)
    if form_data.is_valid():
        form_data.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form_data, 'id': id})
