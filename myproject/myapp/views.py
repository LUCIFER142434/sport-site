from django.shortcuts import render

# Create your views here.
def start(element):
    return render(element,"index.html")