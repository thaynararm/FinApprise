import unittest
from apps.suppliers.models import Suppliers
from django.test import TestCase

class ModelsSuppliersRegisterTestCase(TestCase):

    #Carrega o arquivo com os modelos de Fornecedores
    fixtures = ['fictitious_suppliers']
       
    def test_attributes_model_supplier(self):
        """Verifica se os atributos dos campos do model estão funcionando corretamente quando dados corretos são salvos no banco de dados"""

        #Recupera o modelo de Fornecedor da fixture que possui chave pk = 1
        self.supplier = Suppliers.objects.get(pk=1)

        #Dados esperados pelo teste
        expected_data = {
            "company_name": "Empresa ABC Ltda.",
            "seller_name": "João da Silva",
            "cnpj_cpf": "123.456.789/0001-01",
            "contact": "(11) 98765-4321",
            "uf": "SP",
            "city": "São Paulo",
            "address": "Rua Exemplo, 123",
            "email": "joao.silva@empresaabc.com",
            "observations": "Fornecedor desde 2022",
            "autor": "testuser"
        }

        #Dados informados ao teste
        actual_data = {
            "company_name": self.supplier.company_name,
            "seller_name": self.supplier.seller_name,
            "cnpj_cpf": self.supplier.cnpj_cpf,
            "contact": self.supplier.contact,
            "uf": self.supplier.uf,
            "city": self.supplier.city,
            "address": self.supplier.address,
            "email": self.supplier.email,
            "observations": self.supplier.observations,
            "autor": self.supplier.autor.username,
        }

        #Compara o dicionário de dados esperados com o de dados informados.
        self.assertDictEqual(expected_data, actual_data, "Os campos do modelo de Fornecedores não estão funcionando corretamente")

    def test_checks_accepting_blank_fields(self):
        """Verifica se os campos com blank=True estão aceitando espaços em branco"""     

        #Traz o fornecedor a ser usado no teste
        self.supplier = Suppliers.objects.get(pk=2)
        
        #Traz as informações dos campos configurados com blank=True do fornecedor
        blank_fields = {
            'responsible_name': self.supplier.seller_name,
             'cnpj_cpf': self.supplier.cnpj_cpf,
             'contact': self.supplier.contact, 
             'address': self.supplier.address, 
             'email': self.supplier.email, 
             'observations': self.supplier.observations}

        #Verifica se os campos estão aceitando espaços em branco
        for key, value in blank_fields.items():
            self.assertTrue(value.isspace(), f'O campo {key} do modelo de Fornecedores não está aceitando espaços em branco quando blank=True')

    def test_checks_accepting_null_fields(self):
        """Verifica se os campos com null=True estão aceitando espaços nulos"""
        
        #Traz o fornecedor a ser usado no teste
        self.supplier = Suppliers.objects.get(pk=3)
        
        #Traz as informações dos campos configurados com null=True do fornecedor
        blank_fields = {
            'responsible_name': self.supplier.seller_name,
             'cnpj_cpf': self.supplier.cnpj_cpf,
             'contact': self.supplier.contact, 
             'uf': self.supplier.uf,
             'city': self.supplier.city,
             'address': self.supplier.address, 
             'email': self.supplier.email, 
             'observations': self.supplier.observations}

        #Verifica se os campos estão aceitando espaços nulos
        for key, value in blank_fields.items():
            self.assertTrue(value is None, f'O campo {key} do modelo de Fonercedores não está aceitando espaços nulos quando null=True')

    @unittest.expectedFailure
    def test_checks_duplicate_fields(self):
        """Verifica se os campos com unique=True estão funcionando, a função espera uma falha pois este nome e cnpj já constam no banco de dados, portanto deve dar um erro de duplicidade em um campo com valores únicos"""
    
        #Tenta criar o fornecedor duplicado
        self.supplier_company_name = Suppliers.objects.create(
            company_name = 'Empresa ABC Ltda.',
            cnpj_cpf = '123.456.789/0001-01',
        )

        

        
