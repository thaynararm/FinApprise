import unittest
from django.test import TestCase
from clients.forms import ClientsForms
from clients.fixtures.information_storage import *


class FormsClientsRegisterTestCase(TestCase):


    #Verifica se o formulário está sendo validade quando dados corretos são informados
    def test_validate_form_with_correct_data(self):
        
        #Pega os dados para inserir no formulário
        data = data_for_test_validate_form_with_correct_data
        
        #Insere os dados no formulário
        form = ClientsForms(data=data)

        #Verifica se o formulário é válido
        self.assertTrue(form.is_valid(), f'O formulário não está válido, mas as informações fornecidas estão corretas: {form.errors}')


    #Verifica se o formulário dá erro quando dados incorretos são informados
    @unittest.expectedFailure
    def test_validate_form_with_incorrect_data(self):

        #Pega os dados para inserir no formulário
        data = data_for_test_validate_form_with_incorrect_data
        
        #Insere os dados no formulário
        form = ClientsForms(data=data)

        #Verifica se o formulário é válido
        self.assertTrue(form.is_valid(), f'O formulário está válido, mas as informações fornecidas estão incorretas: {form.errors}')



   