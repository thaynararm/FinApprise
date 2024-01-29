from django.shortcuts import render, redirect
from apps.users.forms import LoginForms
from django.contrib import auth, messages

def login(request):
    #verifica se o usuário está logado e redireciona para o index caso esteja
    if request.user.is_authenticated:
        messages.error(request, 'Usuário logado!')
        return redirect('index')
 
    #se o usuário não estiver logado ele pode acessar a página de login
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request, 'login.html', {'form': form})