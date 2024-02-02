import unittest
from apps.clients.models import Clients
from django.test import TestCase

class ModelsClientsRegisterTestCase(TestCase):

    #Carrega o arquivo com os modelos de Clientsa
    fixtures = ['fictitious_clients']
       
    def test_correct_attributes_model_clients(self):
        """Verifica se os atributos dos campos do model estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

        #Recupera o modelo de Clients da fixture que possui chave pk = 1
        self.client = Clients.objects.get(pk=1)

        #Dados esperados pelo teste
        expected_data = {
            "company_name": "Empresa ABC Ltda.",
            "responsible_name": "João da Silva",
            "cnpj_cpf": "123.456.789/0001-01",
            "contact": "(11) 98765-4321",
            "uf": "SP",
            "city": "São Paulo",
            "address": "Rua Exemplo, 123",
            "email": "joao.silva@empresaabc.com",
            "observations": "Cliente desde 2022",
            "autor": "testuser"
        }

        #Dados informados ao teste
        actual_data = {
            "company_name": self.client.company_name,
            "responsible_name": self.client.responsible_name,
            "cnpj_cpf": self.client.cnpj_cpf,
            "contact": self.client.contact,
            "uf": self.client.uf,
            "city": self.client.city,
            "address": self.client.address,
            "email": self.client.email,
            "observations": self.client.observations,
            "autor": self.client.autor.username,
        }

        #Compara o dicionário de dados esperados com o de dados informados.
        self.assertDictEqual(expected_data, actual_data, "Os campos do modelo de Clientes não estão funcionando corretamente")

    def test_checks_accepting_blank_fields(self):
        """Verifica se os campos com blank=True estão aceitando espaços em branco"""     

        #Traz o cliente a ser usado no teste
        self.client = Clients.objects.get(pk=2)
        
        #Traz as informações dos campos configurados com blank=True do cliente
        blank_fields = {
            'responsible_name': self.client.responsible_name,
             'cnpj_cpf': self.client.cnpj_cpf,
             'contact': self.client.contact, 
             'address': self.client.address, 
             'email': self.client.email, 
             'observations': self.client.observations}

        #Verifica se os campos estão aceitando espaços em branco
        for key, value in blank_fields.items():
            self.assertTrue(value.isspace(), f'O campo {key} do modelo de Clientes não está aceitando espaços em branco quando blank=True')

    def test_checks_accepting_null_fields(self):
        """Verifica se os campos com null=True estão aceitando espaços nulos"""
        
        #Traz o cliente a ser usado no teste
        self.client = Clients.objects.get(pk=3)
        
        #Traz as informações dos campos configurados com null=True do cliente
        blank_fields = {
            'responsible_name': self.client.responsible_name,
             'cnpj_cpf': self.client.cnpj_cpf,
             'contact': self.client.contact, 
             'uf': self.client.uf,
             'city': self.client.city,
             'address': self.client.address, 
             'email': self.client.email, 
             'observations': self.client.observations}

        #Verifica se os campos estão aceitando espaços nulos
        for key, value in blank_fields.items():
            self.assertTrue(value is None, f'O campo {key} do modelo de Clientes não está aceitando espaços nulos quando null=True')

    @unittest.expectedFailure
    def test_checks_duplicate_fields(self):
        """Verifica se os campos com unique=True estão funcionando, a função espera uma falha pois este nome e cnpj já constam no banco de dados, portanto deve dar um erro de duplicidade em um campo com valores únicos"""
    
        #Tenta criar o cliente duplicado
        self.client_company_name = Clients.objects.create(
            company_name = 'Empresa ABC Ltda.',
            cnpj_cpf = '123.456.789/0001-01',
        )

        

        
