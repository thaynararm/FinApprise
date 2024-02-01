from django import forms
from datetime import datetime
from apps.revenues.models import Revenues



class RevenuesForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RevenuesForms, self).__init__(*args, **kwargs)
        self.fields['date_of_competence'].initial = datetime.today().strftime('%Y-%m-%d')
        self.fields['delivery_date'].initial = datetime.today().strftime('%Y-%m-%d')
        self.fields['value'].localize = True
        self.fields['value'].widget.is_localized = True

    

    class Meta:
        model = Revenues        #Especifica quais campos do modelo devem ser incluídos no formulário

        #Especifica quais campos do modelo devem ser incluídos no formulário        
        fields = ['description', 'date_of_competence', 'subcategory', 'source', 'value', 'delivery_date', 'receipt_account', 'receipt_status', 'comments']
            
        #Define os rótulos dos campos
        labels = {
            'description': 'Descrição',
            'date_of_competence': 'Data de Competência',
            'subcategory': 'Categoria',
            'source': 'Origem',
            'value': 'Valor',
            'delivery_date': 'Data de Recebimento',
            'receipt_account': 'Conta de Recebimento',
            'receipt_status': 'Recebido',
            'comments': 'Observações',
            }

        #Define como cada campo deve ser exibido
        widgets = {
            'description': forms.TextInput(attrs={
                'placeholder': 'Descrição da Receita',}),
            'date_of_competence': forms.TextInput(
                attrs={
                'class': 'date'}),
            'subcategory': forms.Select(attrs={
                'id': 'subcategory'}),
            'source': forms.Select(attrs={
                'id': 'source',
                'class': 'combobox'}),
            'value': forms.TextInput(attrs={
                'placeholder': '0,00',
                'class': 'value',
                'step':'0.01',
                'localize': 'True'}),
            'delivery_date': forms.TextInput(
                attrs={
                'class': 'date'}),
            'receipt_account': forms.TextInput(attrs={
                'id': 'receipt_account'}),
            'receipt_status': forms.CheckboxInput(attrs={
                'type': 'checkbox',
            }),
            'comments': forms.TextInput(attrs={
                'placeholder': 'Observações',}),
            }
        
        
    