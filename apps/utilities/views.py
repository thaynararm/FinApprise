from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def name_hello(request):
    """#Retorna o primeiro e último nome do usuário -> usado para adicionar no header"""

    full_name = request.user.get_full_name()

    if full_name:    
        full_name = request.user.get_full_name().split()
        first_name = full_name[0]
        last_name = full_name[-1]
        name = f'{first_name} {last_name}'

        return name
    
    return 'Usuário(a)'