import unittest
from django.test import TestCase
from suppliers.forms import SupplierForms
from suppliers.fixtures.information_storage import *


class FormsSuppliersRegisterTestCase(TestCase):

    def test_validate_form_with_correct_data(self):
        """Verifica se o formulário está sendo validado quando dados corretos são informados"""
        
        #Pega os dados para inserir no formulário
        data = data_for_test_validate_form_with_correct_data
        
        #Insere os dados no formulário
        form = SupplierForms(data=data)

        #Verifica se o formulário é válido
        self.assertTrue(form.is_valid(), f'O formulário não está válido, mas as informações fornecidas estão corretas: {form.errors}')


    @unittest.expectedFailure
    def test_validate_form_with_incorrect_data(self):
        """Verifica se o formulário dá erro quando dados incorretos são informados, a função expera uma falha pois os dados estão incorretos, então deve dar erro"""

        #Pega os dados para inserir no formulário
        data = data_for_test_validate_form_with_incorrect_data
        
        #Insere os dados no formulário
        form = SupplierForms(data=data)

        #Verifica se o formulário é válido
        self.assertTrue(form.is_valid(), f'O formulário está válido, mas as informações fornecidas estão incorretas: {form.errors}')



   