from django.db import models
from apps.clients.models import Clients
from datetime import datetime
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user


class RecipeCategoriesRevenues(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
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
        return self.category_name


class RecipeSubcategoriesRevenues(models.Model):
    category_name = models.ForeignKey(RecipeCategoriesRevenues, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, blank=False, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


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
        return self.subcategory_name


class NewRevenues(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    date_of_competence = models.DateField(default=datetime.now, blank=False, null=False)
    subcategory = models.ForeignKey(RecipeSubcategoriesRevenues, on_delete=models.SET_DEFAULT, default=1)
    source = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, related_name='revenues_source')
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    delivery_date = models.DateField(default=datetime.now, blank=False, null=False)
    receipt_account = models.CharField(max_length=100)
    receipt_status = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='revenues_autor')


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
        return self.description
