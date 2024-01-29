from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user

class Clients(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    responsible_name = models.CharField(max_length=50, blank=True, null=True)
    cnpj_cpf = models.CharField(max_length=19, blank=True, null=True, unique=True)
    contact = models.CharField(max_length=19, blank=True, null=True)
    uf = models.CharField(max_length=2, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Estende o método save para associar o autor ao usuário
    def save(self, *args, **kwargs):
        #Salva o usuário na variável
        current_user = get_current_user()

        #Verifica se foi passado um usuário e se ele está autenticado
        if current_user and current_user.is_authenticated:
            #Atribui o usuário ao campo autor
            self.autor = current_user
        
        #Chama o método save da classe pai e passa todos os argumentos de todos os campos
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name