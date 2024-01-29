from utilities.views import name_hello
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User


class UtilitiesTestCase(TestCase):
    #ambiente de teste
    def setUp(self):
        #é usada para criar instâncias de requisição para simular solicitações HTTP. Isso porque a função name_hello recebe 'request' que é uma resposta HTTP 
        self.factory = RequestFactory()

        #Cria o usuário com as informações necessárias                                
        self.new_user = User.objects.create_user(
            username='testuser', 
            password='testpassword',
            first_name='Test First Name',
            last_name='Test Last Name')
        
        #Força o login do usuário criado
        self.client.force_login(self.new_user)

        #Cria uma instância de requisição GET usando a RequestFactory
        self.request = self.factory.get('/')

        #Atribui o usuário criado à requisição.
        self.request.user = self.new_user

        #Aplica a função name_hello na requisição atribuida ao usuário
        self.name_user = name_hello(self.request)

    #teste da função name_hello
    def test_name_hello_authenticated_user(self):
        """Verifica se a função que insere o nome do usuário no cabeçalho está funcionando quando o usuário está autenticado"""

        self.assertEqual(self.name_user, "Test Name", msg='Os nomes são diferentes')