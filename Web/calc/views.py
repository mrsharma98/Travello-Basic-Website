from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Manish'})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    # fetching the num1 and num2 from the form and performing operation on it.
    result = int(val1) + int(val2)
    return render(request, 'result.html', {'result': result})
