from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Evenement
from .models import Category
from django.views.generic import ListView,DetailView




class EvenmentView(ListView):
    model=Evenement
    template_name='evenment/evenment_list.html'
    context_object_name='evenment'


class EvenmentDetailView(DetailView):
    model=Evenement
    template_name='evenment/evenment_Detail_list.html'
    context_object_name='evenment'


class categorieView(ListView):
    model=Category
    template_name='categorie/categorie_list.html'
    context_object_name='categorie'

class categorieDetailView(DetailView):
    model=Category
    template_name='categorie/categorie.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        context['evenment'] = Evenement.objects.filter(category=category)
        return context

class EvenmentCreation(ListView):
    model=Evenement
    template_name='cree/cree.html'
    context_object_name='cree'

