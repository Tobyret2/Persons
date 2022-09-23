from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PersonForm
from django.urls import reverse_lazy

from .models import Person

def view_all(request):
    persons = Person.objects.all()
    return render(request,'vp/index.html',{'persons':persons})

class PersonCreatView(CreateView):
   template_name = 'vp/create.html'
   form_class = PersonForm
   success_url = reverse_lazy('view_all')