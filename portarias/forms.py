from django import forms
from django.forms import ModelForm
from portarias.models import Visitantes


class VisitForm(ModelForm):
    class Meta:
        model = Visitantes

        tipo_visitantes = {
            '': '',
            'AJUDANTE': 'AJUDANTE',
            'FUNCIONÁRIO SJK': 'FUNCIONÁRIO SJK',
            'MOTORISTA': 'MOTORISTA',
            'PRESTADOR DE SERVIÇO': 'PRESTADOR DE SERVIÇO',
            'VISITANTE': 'VISITANTE'
        }

        tipo_veiculos = {
            '': '',
            'CAMINHÃO': 'CAMINHÃO',
            'CARRETA': 'CARRETA',
            'CARRO': 'CARRO',
            'MOTO': 'MOTO',
            'REBOQUE': 'REBOQUE'
        }

        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome...'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa...'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF...'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG...'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone...'}),
            'tipo_visitante': forms.Select(attrs={'class': 'form-control'}, choices=tipo_visitantes),
            'tipo_veiculo': forms.Select(attrs={'class': 'form-control'}, choices=tipo_veiculos),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo...'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa...'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor...'}),
            'placa_reboque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa do reboque...'}),
            'objetos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objetos...'}),
            'observacoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observações...'}),
        }
