import unittest
from django.test import TestCase
from apps.revenues.models import *
from datetime import date
from apps.revenues.fixtures.information_storage import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class BaseTestCase(TestCase):
    """Serve como base para todos as classes de testes que vamos usar"""

    fixtures = ['fictitious_revenues']


class ModelsRecipeCategoriesRevenuesTestCase(BaseTestCase):
    """Contém todos os testes referentes à classe RecipeCategoriesRevenues do modelo de receitas"""

    def test_correct_attributes_model_categories(self):
        """Verifica se os atributos dos campos do model de categoria estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

        self.category = RecipeCategoriesRevenues.objects.get(pk=1)

        expected_data = expected_data_for_test_correct_attributes_model_categories

        actual_data = {
            "category_name": self.category.category_name,
            "autor": self.category.autor.username,
        }

        self.assertEqual(expected_data, actual_data, f'Os campos do modelo de categorias das receitas (Revenues/RecipeCategoriesRevenues) não estão funcionando corretamente')

    def test_blank_attributes_model_categories(self):
        """Verifica se os atributos dos campos com blank = False do model de categoria estão aceitando valore em branco"""

        self.autor = User.objects.get(pk=1)

        with self.assertRaises(ValidationError, msg='O campo category_name do app revenues está aceitando valores em branco'):
            self.category_blank = RecipeCategoriesRevenues.objects.create(
                category_name = "",
                autor = self.autor,)

            self.category_blank.full_clean()

        
    # @unittest.expectedFailure
    # def test_null_attributes_model_categories(self):
    #     """Verifica se os atributos dos campos com null = False do model de categoria estão aceitando valore nulos"""

    #     self.autor = User.objects.get(pk=1)

    #     with self.assertRaises(ValidationError, 'O campo category_name do app revenues está aceitando valores nulos'):
            self.category_null = RecipeCategoriesRevenues.objects.create(
                category_name = None,
                autor = self.autor,)

    def test_checks_duplicate_fields_categories(self):
        """Verifica se os campos com unique=True estão funcionando, a função espera uma falha pois esta categoria já consta no banco de dados, portanto deve dar um erro de duplicidade em um campo com valores únicos"""
    
        self.autor = User.objects.get(pk=1)

        with self.assertRaises(IntegrityError, msg='O campo category_name do app revenues está aceitando valores nulos'):
            #Tenta criar o cliente duplicado
            self.category_name = RecipeCategoriesRevenues.objects.create(
                category_name = 'Receitas', 
                autor = self.autor)

    
class ModelsRecipeSubcategoriesRevenuesTestCase(BaseTestCase):
    """Contém todos os testes referentes à classe RecipeSubcategoriesRevenues do modelo de receitas"""
    
    def test_correct_attributes_model_subcategories(self):
        """Verifica se os atributos dos campos do model de subcategoria estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

        self.subcategory = RecipeSubcategoriesRevenues.objects.get(pk=1)

        expected_data = expected_data_for_test_correct_attributes_model_subcategories

        actual_data = {
            "category_name": self.subcategory.category_name.category_name,
            "subcategory_name": self.subcategory.subcategory_name,
            "autor": self.subcategory.autor.username,
        }

        self.assertEqual(expected_data, actual_data, f'Os campos do modelo de subcategorias das receitas (Revenues/RecipeSubcategoriesRevenues) não estão funcionando corretamente')

    def test_blank_attributes_model_subcategories(self):
        """Verifica se os atributos dos campos com blank = False do model de subcategoria estão aceitando valore em branco"""

        self.autor = User.objects.get(pk=1)
        self.category = RecipeCategoriesRevenues.objects.get(pk=1)

        with self.assertRaises(ValidationError, msg='O campo category_name do app revenues está aceitando valores em branco'):
            self.subcategory_blank = RecipeSubcategoriesRevenues.objects.create(
                category_name = self.category,
                subcategory_name = "",
                autor = self.autor,)

            self.subcategory_blank.full_clean()
    
    def test_checks_duplicate_fields_subcategories(self):
        """Verifica se os campos com unique=True estão funcionando, a função espera uma falha pois esta subcategoria já consta no banco de dados, portanto deve dar um erro de duplicidade em um campo com valores únicos"""
    
        self.autor = User.objects.get(pk=1)
        self.category = RecipeCategoriesRevenues.objects.get(pk=1)

        with self.assertRaises(IntegrityError, msg='O campo category_name do app revenues está aceitando valores em branco'):
            #Tenta criar o objeto duplicado
            self.category_name = RecipeSubcategoriesRevenues.objects.create(
                category_name = self.category,
                subcategory_name = "Receitas de Vendas",
                autor = self.autor)


class ModelsNewRevenuesTestCase(BaseTestCase):
    """Contém todos os testes referentes à classe NewRevenues do modelo de receitas"""
    
    def test_correct_attributes_model_new_revenues(self):
        """Verifica se os atributos dos campos do model de nova receita estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

        self.revenue = NewRevenues.objects.get(pk=1)

        expected_data = expected_data_for_test_correct_attributes_model_newrevenues

        actual_data = {
            "description": self.revenue.description,
            "date_of_competence": self.revenue.date_of_competence.strftime('%Y-%m-%d'),
            "subcategory": self.revenue.subcategory.subcategory_name,
            "source": self.revenue.source.company_name,
            "value": float(self.revenue.value),
            "delivery_date": self.revenue.delivery_date.strftime('%Y-%m-%d'),
            "receipt_account": self.revenue.receipt_account,
            "receipt_status": self.revenue.receipt_status,
            "comments": self.revenue.comments,
            "autor": self.revenue.autor.username,
        }

        self.assertEqual(expected_data, actual_data, f'Os campos do modelo de receitas das receitas (Revenues/NewRevenue) não estão funcionando corretamente')

    def test_blank_attributes_model_new_revenues(self):
        """Verifica se os atributos dos campos com blank = False do model de categoria estão aceitando valore em branco"""

        self.autor = User.objects.get(pk=1)
        self.subcategory = RecipeSubcategoriesRevenues.objects.get(pk=1)

        with self.assertRaises(ValidationError, msg='Os campos do app revenues estão aceitando valores em branco'):
            self.newrevenue_blank = NewRevenues.objects.create(
                description = "",
                date_of_competence = "",
                subcategory = self.subcategory,
                value = "",
                delivery_date = "",                
                autor = self.autor,)

            self.newrevenue_blank.full_clean()
    
    def test_null_attributes_model_new_revenues(self):
        """Verifica se os atributos dos campos com null = False do model de categoria estão aceitando valore em branco"""

        self.autor = User.objects.get(pk=1)
        self.subcategory = RecipeSubcategoriesRevenues.objects.get(pk=1)

        with self.assertRaises(IntegrityError, msg='Os campos do app revenues estão aceitando valores nulos'):
            self.newrevenue_blank = NewRevenues.objects.create(
                description = None,
                date_of_competence = None,
                value = None,
                delivery_date = None,
                subcategory = self.subcategory,
                autor = self.autor,)

    