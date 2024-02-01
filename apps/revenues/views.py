from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.revenues.forms import RevenuesForms
from apps.utilities.views import name_hello


@login_required(login_url='login')
def new_revenue(request):    
    #Exibe e instancia o formulário
    revenues_form = RevenuesForms() 

    if request.method == 'POST':
        revenues_form = RevenuesForms(request.POST)

        #Verifica se o formulário é valido e salva no banco de dados
        if revenues_form.is_valid():
                try:
                    revenues_form.save()
                    messages.success(request, 'Nova receita registrada!')
                    return redirect('index')
                except:
                    messages.error(request, 'Ocorreu um erro ao cadastrar a receita!')

        else:
             messages.error(request, 'Ocorreu um erro ao cadastrar a receita!')
             print(revenues_form.errors)
                         
    name = name_hello(request)
    return render(request, 'new_revenue.html', {'revenues_form': revenues_form, 'name': name})


