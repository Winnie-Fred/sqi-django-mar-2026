from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def sign_up(request):
    messages.debug(request, "Account created successfully")
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("users:login")

    context = {"form": form}
    return render(request, "users/sign-up.html", context)