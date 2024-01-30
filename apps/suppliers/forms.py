import docbr 
from django import forms
from apps.suppliers.models import Suppliers

class SupplierForms(forms.ModelForm):
    class Meta:
        model = Suppliers    #Especifica quais campos do modelo devem ser incluídos no formulário

        #Especifica quais campos do modelo devem ser incluídos no formulário
        fields = ['company_name', 'cnpj_cpf', 'seller_name', 'contact','uf', 'city', 'address', 'email', 'observations']
            
        #Define os rótulos dos campos
        labels = { 
            'company_name': 'Nome da empresa',
            'cnpj_cpf': 'CNPJ ou CPF',
            'seller_name': 'Nome do Vendedor da Empresa',
            'contact': 'Número de Contato',
            'uf': 'Estado',
            'city': 'Cidade',
            'address': 'Endereço do Cliente',
            'email': 'Email',
            'observations': 'Observações'
        }

        #Define como cada campo deve ser exibido
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome da empresa',}),
            'cnpj_cpf': forms.TextInput(attrs={
                'placeholder': 'Digite o CNPJ da empresa ou CPF do responsável',}),
            'seller_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do responsável pela empresa',}),
            'contact': forms.TextInput(attrs={
                'placeholder': '(xx) xxxxx-xxxx',}),
            'uf': forms.Select(attrs={
                'class': 'state-field',
                'id': 'uf'}),
            'city': forms.Select(attrs={
                'class': 'city-field',
                'id': 'city'}),
            'address': forms.TextInput(attrs={
                'placeholder': 'Digite o endereço da empresa ou do responsável',}),
            'email': forms.TextInput(attrs={
                'placeholder': 'exemplo@email.com',}),
            'observations': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
        }

        
    def clean_contact(self):
        """Cria uma máscara padrão para salvar os contatos no banco de dados"""
    
        #Recupera o contato renderizado
        contact = self.cleaned_data['contact']

        #Verifica se o usuário foi inserido e se está com 11 dígitos para então aplicar o padrão
        if contact is not None:
            if len(contact) == 11:
                list_contact = list(contact)
                a = ''.join(list_contact[0:2])
                b = ''.join(list_contact[2:7])
                c = ''.join(list_contact[7:])
                contact = f'+55 ({a}) {b}-{c}'

                return contact
            
            raise forms.ValidationError("O contato deve conter 11 dígitos, DDD + Número de Telefone")

        return contact

    def clean_cnpj_cpf(self):
        """Cria uma máscara padrão para salvar o CNPJ ou CPF no banco de dados"""
        
        #Recupera o cnpj ou cpf renderizado
        cnpj_cpf = self.cleaned_data['cnpj_cpf']

        #Verifica se o campo não é vazio
        if cnpj_cpf is not None:
            
            #Cria a máscara para o CNPJ
            if len(cnpj_cpf) == 14:
                if docbr.validate(cnpj_cpf, doctype='cnpj', lazy=False):
                    list_cnpj = list(cnpj_cpf)
                    a = ''.join(list_cnpj[0:2])
                    b = ''.join(list_cnpj[3:6])
                    c = ''.join(list_cnpj[6:9])
                    d = ''.join(list_cnpj[9:13])
                    e = ''.join(list_cnpj[13:])
                    cnpj = f'{a}.{b}.{c}/{d}-{e}'

                    return cnpj
                
                raise forms.ValidationError("Insira um CNPJ válido")
            
            #Cria a máscara para o CPF
            if len(cnpj_cpf) == 11:
                if docbr.validate(cnpj_cpf, doctype='cpf', lazy=False):
                    list_cpf = list(cnpj_cpf)
                    a = ''.join(list_cpf[0:3])
                    b = ''.join(list_cpf[3:6])
                    c = ''.join(list_cpf[6:9])
                    d = ''.join(list_cpf[9:]) 
                    cpf = f'{a}.{b}.{c}-{d}' 

                    return cpf
                
                raise forms.ValidationError("Insira um CPF válido")
            
            raise forms.ValidationError("Insira um CNPJ ou um CPF válido")

        return cnpj_cpf
            
