from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def second_app_view(request):
    return HttpResponse("Second App View")