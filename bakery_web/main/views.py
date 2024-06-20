from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/nav/nav_about.html')

def contact(request):
    return render(request, 'main/nav/nav_contact.html')

def reviews(request):
    return render(request, 'main/nav/nav_reviews.html')

def products(request):
    return render(request, 'main/nav/nav_products.html')