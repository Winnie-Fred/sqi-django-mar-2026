from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello_page(request):
    return HttpResponse("<h1>Hello from Winnie</h1>")


def second_view(request):
    return HttpResponse("This is the second view of the first app")