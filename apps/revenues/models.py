from django.db import models
from apps.clients.models import Clients
from datetime import datetime
from django.contrib.auth.models import User


class RecipeCategoriesRevenues(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.category_name

class RecipeSubcategoriesRevenues(models.Model):
    category_name = models.ForeignKey(RecipeCategoriesRevenues, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, blank=False, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.subcategory_name


class Revenues(models.Model):
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


    def __str__(self):
        return self.description
