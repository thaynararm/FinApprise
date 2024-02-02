import unittest
from django.test import TestCase
from apps.revenues.models import *
from datetime import date
from apps.revenues.fixtures.information_storage import *


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

    @unittest.expectedFailure
    def test_blank_attributes_model_categories(self):
        """Verifica se os atributos dos campos com blank = False do model de categoria estão aceitando valore em branco"""

        self.autor = User.objects.get(pk=1)

        self.category_blank = RecipeCategoriesRevenues.objects.create(
            category_name = "",
            autor = self.autor,)

        self.category_blank.full_clean()
    
    @unittest.expectedFailure
    def test_null_attributes_model_categories(self):
        """Verifica se os atributos dos campos com null = False do model de categoria estão aceitando valore nulos"""

        self.autor = User.objects.get(pk=1)

        self.category_null = RecipeCategoriesRevenues.objects.create(
            category_name = None,
            autor = self.autor,)


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


class ModelsNewRevenuesTestCase(BaseTestCase):
    """Contém todos os testes referentes à classe NewRevenues do modelo de receitas"""
    
    def test_correct_attributes_model_revenues(self):
        """Verifica se os atributos dos campos do model de categoria estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

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

