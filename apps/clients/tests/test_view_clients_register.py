import unittest
from django.test import TestCase
from clients.fixtures.information_storage import data_for_test_validate_form_with_correct_data
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from apps.clients.models import Clients
from django.db.utils import IntegrityError



class ViewsClientsRegisterTestCase(TestCase):

    #Cria o ambiente de testes
    def setUp(self):
        self.list_url = reverse('register_client')

        self.new_user = User.objects.create_user(
            username='testuser', 
            password='testpassword',
            first_name='Test First Name',
            last_name='Test Last Name')
        
        #Força o login do usuário criado
        self.client.force_login(self.new_user)


    #Verifica se está sendo redirecionado para a página de index ao enviar o formulário com um usuário sem autenticação
    def test_status_code_when_submitted_logged(self):

        #Pega as informações corretas para solicitar o POST
        data = data_for_test_validate_form_with_correct_data

        #Solicita o Post
        response = self.client.post(self.list_url, data=data)

        #Pega a url de redirecionamento após a solicitação do POST
        redirect_url = response.url

        #Faz a verificação do teste
        self.assertEqual('/', redirect_url, f'A solicitação de POST não foi bem sucedida, á pagina está indo para {redirect_url}')


    #Verifica se está sendo redirecionado para a página de login ao enviar o formulário com um usuário sem autenticação 
    def test_status_code_when_submitted_logged_out(self):

        #Pega as informações corretas para solicitar o POST
        data = data_for_test_validate_form_with_correct_data

        #Faz o logout do usuário para a função ser validada
        self.client.logout()

        #Solicita o Post
        response = self.client.post(self.list_url, data=data)

        #Pega a url de redirecionamento após a solicitação do POST
        redirect_url = response.url

        #Faz a verificação do teste
        self.assertEqual('/login/?next=/register_client/', redirect_url, f'A página não está sendo redirecionada para a página de login, está indo para {redirect_url}')


    #Verifica se está sendo redirecionado para a página de login ao enviar o formulário com um usuário sem autenticação 
    def test_message_error_company_registered(self):

        #Cria um objeto
        self.object = Clients.objects.create(company_name="Empresa de Teste", autor=self.new_user)

        #Pega as informações corretas para solicitar o POST
        data = data_for_test_validate_form_with_correct_data

        #Tenta fazer o post do objeto com o mesmo nome do criado acima
        response = self.client.post(self.list_url, data=data)
        
        #response.wsgi_request contém informações sobre a solicitação feita no teste e get_messages() é uma função que recupera as mensagens armazenadas durante uma solicitação, então essa parte está iterando sobre todas as mensagens sobre a solicitação e transformando-as em string
        messages = [str(message) for message in get_messages(response.wsgi_request)]

        #Verifica se a mensagem configurada na view está dentro das mensagens recuperadas acima
        self.assertIn('Nome da empresa já cadastrado!', messages)
        
        
    