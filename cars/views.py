from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from cars.models import Car
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.forms import CarModelForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView


# Create your views here.

#função para pesquisar carros dentro da pagina 

# def car_views(request):
#     cars= Car.objects.all()
#     search= request.GET.get('search')
   
#     if search:
#         cars=Car.objects.filter(model__icontains=search)
    
#     return render(request, 'cars.html',
#                   {'cars':  cars} )



#classe para visualizar os carros


# class CarViews(View):


#     def get(self,request):
#         cars= Car.objects.all()
#         search= request.GET.get('search')
   
#         if search:
#             cars=Car.objects.filter(model__icontains=search)
        
#         return render(request, 'cars.html',
#    
#              {'cars':  cars} )
#abaixo um jeito mais facil de escrever esta classe CarViews
    

class CarListView(ListView):
    model= Car
    template_name='cars.html'
    context_object_name= 'cars'

    def get_queryset(self):
        cars= super().get_queryset().order_by('model')
        search= self.request.GET.get('search')
        if search:
            cars= cars.filter(model__icontains=search)
        return cars                   

#função para cadastrar um novo carro e validar se o formulario foi preenchido corretamente.                     
# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form= CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#         return redirect ('car_views')

#     else:
#         new_car_form= CarModelForm()
#     return render (request, 'new_car.html', {'new_car_form': new_car_form})


#classe para cadastrar um novo carro

# class NewCarView(View):

#     def get(self, request):
#         new_car_form= CarModelForm()
#         return render (request, 'new_car.html', {'new_car_form': new_car_form})
    


#     def post(self,request):
#         new_car_form=CarModelForm(request.POST,request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('car_views')
#         else:
#             return render (request, 'new_car.html', {'new_car_form': new_car_form})

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarListView(CreateView):
        model= Car
        form_class= CarModelForm
        template_name='new_car.html'
        success_url= '/cars/'


class CarDetailView(DetailView):
    model= Car
    template_name='car_detail.html'


class CarUpdateView(UpdateView):
     model= Car
     form_class= CarModelForm
     template_name='car_update.html'
     
     def get_success_url(self):
          return reverse_lazy ('detail',kwargs={'pk':self.object.pk})


class CarDeleteView(DeleteView):
     model= Car
     template_name= 'car_delete.html'
     success_url= '/cars/'
