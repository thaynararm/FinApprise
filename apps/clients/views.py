from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.clients.models import Clients
from apps.clients.forms import ClientsForms
from apps.utilities.views import name_hello


@login_required(login_url='login')
def register_client(request): 
    """Exibe a view do registro de clientes e verifica os dados inseridos pelo usuário"""

    #Instancia o formulário e verifica se a requisição é do tipo POST
    clients_form = ClientsForms() 
    if request.method == 'POST':

        #Cria uma instância do formulário utilizando os dados recebidos e recupera o nome do nome da empresa
        clients_form = ClientsForms(request.POST)
        new_company_name = request.POST['company_name']

        #Verifica se o nome do cliente já está cadastrado e exibe uma mensagem de erro caso esteja
        if Clients.objects.filter(company_name=new_company_name).exists():
            messages.error(request, 'Nome da empresa já cadastrado!')

        #Verifica se o formulário é valido e salva no banco de dados, caso não seja válido insere uma mensagem de erro ao usuário e mostra no console o erro
        if clients_form.is_valid():
            try:
                clients_form.save()
                messages.success(request, 'Novo cliente cadastrado!')
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Ocorreu um erro ao cadastrar o cliente!')
                print(e)
    
    #Insere o nome do usuário no header e renderiza a view
    name = name_hello(request)
    return render(request, 'register_clients.html', {'clients_form': clients_form, 'name': name})


