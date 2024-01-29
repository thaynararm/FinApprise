from django.contrib.auth.decorators import login_required

#Retorna o primeiro e último nome do usuário -> usado para adicionar no header
@login_required(login_url='login')
def name_hello(request):

    full_name = request.user.get_full_name()

    if full_name:    
        full_name = request.user.get_full_name().split()
        first_name = full_name[0]
        last_name = full_name[-1]
        name = f'{first_name} {last_name}'

        return name
    
    return 'Usuário(a)'