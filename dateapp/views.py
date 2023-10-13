import django.urls
from django.shortcuts import render,redirect
from .models import date
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from.forms import todoform


class Tasklistview(ListView):
    model=date
    template_name = 'pranav.html'
    context_object_name = 'pranavs'
class Taskdetailview(DetailView):
    model = date
    template_name ='pranav2.html'
    context_object_name ='task2'
class TaskUpdateview(UpdateView):
    model = date
    template_name = 'update.html'
    context_object_name = 'task3'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DetailView):
    model = date
    template_name ='delete.html'
    succuss_url = reverse_lazy('cbvhome')



def add(requset):
    date1=date.objects.all()
    if requset.method=='POST':
        name=requset.POST.get('name','')
        priority1=requset.POST.get('priority','')
        dates=requset.POST.get('date','')
        pranav=date(name=name,priority=priority1,date=dates)
        pranav.save()
    return render(requset,'pranav.html',{'pranavs':date1})
def delete(requset,taskid):
    task=date.objects.get(id=taskid)
    if requset.method=='POST':
        task.delete()
        return redirect('/')
    return render(requset,'delete.html')
def update(request,id):
    task=date.objects.get(id=id)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})

