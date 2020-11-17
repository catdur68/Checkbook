from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "home.html", context)

def balance(request):
    accounts = request.accounts
    context = {
        'accounts': accounts,
    }
    return render(request, "balance.html", context)