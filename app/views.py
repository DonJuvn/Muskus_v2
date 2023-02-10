
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render
from .models import Product, Category


class Search(ListView):
	def get_queryset(self):
		return Product.objects.filter(title__icontains=self.request.GET.get("g"))

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(self, *args, **kwargs)
		context["q"] = self.request.GET.get("q")
		return context

def home(request):
    return render(request, "home.html")


def men(request):
	a = Product.objects.filter(category_id='1')
	context = {'a': a}
	return render(request, 'men.html', context)


def uni(request):
	c = Product.objects.filter(category_id='3')
	context = {'c': c}
	return render(request, 'uni.html', context)

def women(request):
	b = Product.objects.filter(category_id='2')
	context = {'b': b}
	return render(request, 'women.html', context)