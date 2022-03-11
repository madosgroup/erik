from django.shortcuts import render
from django.views.generic import CreateView
from django import forms
from .models import *
SEX = categories
class CustomerUserForm(forms.ModelForm):
	proprietaire  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	# Type  = forms.CharField(
 #        widget=forms.S(attrs={'class': 'form-ceontrol '}),
 #        max_length=255)
	plaque  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	Numero_chasis  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	Adresse  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	CNI  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	Adresse  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	Telephone  = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','required':'True'}),
        max_length=255)
	Type=forms.ChoiceField(choices=SEX,widget=forms.Select(attrs={"name": "Type	",'class':'form-control'}))
	class Meta:
	    model = Moto
	    fields = [
        'proprietaire',
        'Type',
        'plaque',
        'Numero_chasis',
        'Adresse',
        'CNI',
        'Adresse',
        'Telephone',
        ]
# class CreateArticle(CreateView):
# 	model = Moto
# 	form_class = CustomerUserForm
# 	# fields =('__all__')

# 	def form_valid(self, form):
# 	    return super(CreateArticle, self).form_valid(form)

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, View, UpdateView, FormView,CreateView

 
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    sum_of_bajaj = Moto.objects.all().filter(Type='BAJAJ').count()
    sum_of_moto = Moto.objects.all().filter(Type='MOTO').count()
    # add the dictionary during initialization
    form = CustomerUserForm(request.POST or None)
    
    if form.is_valid():
        form.save()
          
    context['form']= form
    context['sum_of_bajaj']= sum_of_bajaj
    context['sum_of_moto']= sum_of_moto
    return render(request, "home/moto_form.html", context)



from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class HomeView(ListView):
    """ Home View Definition """

    model = Moto
    paginate_by = 10
    # ordering = "created"
    ordering = "-id"
    paginate_orphans = 10
    context_object_name = "Moto"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        list_vh =Moto.objects.filter(Type='Bikes')
        paginator = Paginator(list_vh, self.paginate_by)
        page = self.request.GET.get('page')
        file_exams = paginator.page(page)
        sum_of_bajaj = Moto.objects.all().filter(Type='BAJAJ').count()
        sum_of_moto = Moto.objects.all().filter(Type='MOTO').count()
        context.update({'sum_of_bajaj': sum_of_bajaj})
        context.update({'sum_of_moto': sum_of_moto})
        context['list_exams'] = file_exams
        return context





class BikesView(ListView):
    """ Home View Definition """

    model = Moto
    paginate_by = 10
    # ordering = "created"
    ordering = "-id"
    paginate_orphans = 10
    context_object_name = "Moto"
    def get_context_data(self, **kwargs):
        context = super(BikesView, self).get_context_data(**kwargs)
        list_vh =Moto.objects.filter(Type='MOTO')
        paginator = Paginator(list_vh, self.paginate_by)
        page = self.request.GET.get('page')
        file_exams = paginator.page(page)
        sum_of_bajaj = Moto.objects.filter(Type='BAJAJ').count()
        sum_of_moto = Moto.objects.filter(Type='MOTO').count()
        context.update({'sum_of_bajaj': sum_of_bajaj})
        context.update({'sum_of_moto': sum_of_moto})
        context['list_exams'] = file_exams
        context['object_list'] = list_vh
        context['name'] = 'Moto'
        context['link'] = 'MotoView'
        return context
class BajajView(ListView):
    """ Home View Definition """

    model = Moto
    paginate_by = 10
    # ordering = "created"
    ordering = "-id"
    paginate_orphans = 10
    context_object_name = "Moto"
    def get_context_data(self, **kwargs):
        context = super(BajajView, self).get_context_data(**kwargs)
        list_vh =Moto.objects.filter(Type='BAJAJ')
        paginator = Paginator(list_vh, self.paginate_by)
        page = self.request.GET.get('page')
        file_exams = paginator.page(page)
        sum_of_bajaj = Moto.objects.filter(Type='BAJAJ').count()
        sum_of_moto = Moto.objects.filter(Type='MOTO').count()
        context.update({'sum_of_bajaj': sum_of_bajaj})
        context.update({'sum_of_moto': sum_of_moto})
        context['list_exams'] = file_exams
        context['object_list'] = list_vh
        context['name'] = 'Bajaj'
        context['link'] = 'bajajiView'
        return context


def search(request):
        q = request.GET['q']
        name = Moto.objects.filter(Numero_chasis__icontains=q)
        context={}
        context['object_list']=name
        return render(request,'home/moto_list.html',context)






class bajajiView(ListView):
    """ Home View Definition """

    model = Moto
    ordering = "-created"
    ordering = "-id"
    def get_context_data(self, **kwargs):
        context = super(bajajiView, self).get_context_data(**kwargs)
        list_vh =Moto.objects.filter(Type='BAJAJ')
        sum_of_bajaj = Moto.objects.filter(Type='BAJAJ').count()
        sum_of_moto = Moto.objects.filter(Type='MOTO').count()
        context.update({'sum_of_bajaj': sum_of_bajaj})
        context.update({'sum_of_moto': sum_of_moto})
        context['object_list'] = list_vh
        context['name'] = 'Bajaj'
        context['link'] = 'bajajiView'
        return context






class MotoView(ListView):
    """ Home View Definition """

    model = Moto
    paginate_by = 10
    ordering = "-created"
    ordering = "-id"