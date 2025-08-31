from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login


def signUp(request):

    if request.method == "POST":

        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("new_chat")
    else:
        form = forms.SignUpForm()
    return render(request, "registration/register.html", {"form": form})
