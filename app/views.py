from django.shortcuts import render



def home(request):
	return render(request, 'home.html')

def men(request):
	return render(request, 'men.html')

def uni(request):
	return render(request, 'uni.html')

def women(request):
	return render(request, 'women.html')