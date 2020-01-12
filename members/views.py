from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

from members.form import SignupForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.signup()
            login(request, user)
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)
