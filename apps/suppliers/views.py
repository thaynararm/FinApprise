from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.suppliers.models import Suppliers
from apps.suppliers.forms import SupplierForms
from apps.utilities.views import name_hello

@login_required(login_url='login')
def register_supplier(request):
    """Exibe a view do registro de fornecedores e verifica os dados inseridos pelo usuário"""

    #Instancia o formulário e verifica se a requisição é do tipo POST
    supplier_form = SupplierForms()
    if request.method == 'POST':

        #Cria uma instância do formulário utilizando os dados recebidos e recupera o nome do nome da empresa
        supplier_form = SupplierForms(request.POST)
        new_company_name = request.POST['company_name']

        #Verifica se o nome do fornecedor já está cadastrado e exibe uma mensagem de erro caso esteja
        if Suppliers.objects.filter(company_name=new_company_name).exists():
            messages.error(request, 'Nome da empresa já cadastrado!')            
     
        #Verifica se o formulário é valido e salva no banco de dados, caso não seja válido insere uma mensagem de erro ao usuário e mostra no console o erro
        if supplier_form.is_valid():
            try:
                supplier_form.save()
                messages.success(request, 'Novo fornecedor cadastrado!')
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Ocorreu um erro ao cadastrar o fornecedor!')
                print(e)

    #Insere o nome do usuário no header e renderiza a view
    name = name_hello(request)
    return render(request, 'register_supplier.html', {'supplier_form': supplier_form, 'name': name})


