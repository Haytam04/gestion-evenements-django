from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Evenement
from .models import Category
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class creationView(View):
    
    def post(self,request):
    
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        nombre_places = request.POST.get('nombre_places')
        statue = request.POST.get('statue')
        lieu = request.POST.get('lieu')
        date = request.POST.get('date')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

        
        try:
            
            nombre_places = int(nombre_places)
            if nombre_places > 1000:
                messages.error(request, "Maximum 1000 places allowed")
                return redirect('creation')

            
            category = Category.objects.get(id=category_id)



            
            evenement = Evenement.objects.create(
                name=name,
                category=category,
                nombre_places=nombre_places,
                statue=statue,
                lieu=lieu,
                date=date,
                description=description,
                image=image,
            )

            messages.success(request, "Event created successfully!")
            return redirect('evenment')  

        except Category.DoesNotExist:
            messages.error(request, "Invalid category selected")
            return redirect('cree')
        except ValueError:
            messages.error(request, "Invalid number of places")
            return redirect('cree')
        except Exception as e:
            messages.error(request, f"Error creating event: {str(e)}")
            return redirect('cree')



class editpageView(UpdateView):
    
    model = Evenement
    template_name = 'cree/cree.html'
    fields = ['name', 'category', 'date', 'lieu', 'nombre_places', 'statue', 'image', 'description']
    success_url = reverse_lazy('evenment') 
#retour
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #dictiomaire
        context['categories'] = Category.objects.all()
        context['event'] = self.object  
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['event'] = self.object  # Make the event available in template as 'event'
        return context


def delete_item(request, pk):
    item = get_object_or_404(Evenement, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('evenment')  
    return redirect('evenment')  




