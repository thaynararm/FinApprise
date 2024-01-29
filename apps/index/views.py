from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.utilities.views import name_hello

@login_required(login_url='login')
def index(request):
    name = name_hello(request)
    return render(request, 'index.html', {'name':name})