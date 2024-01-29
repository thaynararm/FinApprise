from django.test import TestCase
from django.contrib.auth.models import User


class UtilitiesTestCase(TestCase):
    #ambiente de teste
    def setUp(self):
        '''Cria um cliente para atuar como um navegador da Web fictício, permite testar visualizações e interagir com o aplicativo'''
       
       #Cria o usuário com as informações necessárias    
        self.new_user = User.objects.create_user(
            username='testuser', 
            password='testpassword')

    #teste para um login bem sucedido
    def test_successful_login(self):
        '''Verifica se o login foi bem sucedido'''

        #Traz a resposta da tentaiva de login
        response = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(response, msg='O Login falhou')


    #teste para login com username incorreto
    def test_successful_username(self):
        '''Verifica se o username está incorreto'''

        #Traz a resposta da tentaiva de login
        response = self.client.login(username='testuserfail', password='testpassword')
        self.assertFalse(response, msg='Falha na verificação do Username')


    #teste para login com password incorreto
    def test_successful_password(self):
        '''Verifica se o username está incorreto'''

        #Traz a resposta da tentaiva de login
        response = self.client.login(username='testuser', password='testpasswordfail')
        self.assertFalse(response, msg='Falha na verificação da Senha')
