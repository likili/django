from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, "index.html")

def instructors_list(request):
    return render(request, "instructors.html")

def hello_python(request):
    return render(request, "python.html")

def http(request):
    response = render(request, "http.html")
    response['Age'] = 2000
    response.status_code = 404
    return response

def sum_two(request, a, b):
    s = int(a)+int(b)
    return HttpResponse(s)
