from django.db import models

AJUDANTE = 'AJUDANTE'
FUNCIONARIO_SJK = 'FUNCIONÁRIO SJK'
MOTORISTA = 'MOTORISTA'
PRESTADOR_DE_SERVICO = 'PRESTADOR DE SERVIÇO'
VISITANTE = 'VISITANTE'
tipo_visitantes = (
    (AJUDANTE, 'Ajudante'),
    (FUNCIONARIO_SJK, 'Funcionário SJK'),
    (MOTORISTA, 'Motorista'),
    (PRESTADOR_DE_SERVICO, 'Prestador de Serviço'),
    (VISITANTE, 'Visitante'),
)

CAMINHAO = 'CAMINHÃO'
CARRETA = 'CARRETA'
CARRO = 'CARRO'
MOTO = 'MOTO'
REBOQUE = 'REBOQUE'
tipo_veiculos = (
    (CAMINHAO, 'Caminhão'),
    (CARRETA, 'Carreta'),
    (CARRO, 'Carro'),
    (MOTO, 'Moto'),
    (REBOQUE, 'Reboque'),
)


# Create your models here.
class Visitantes(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    rg = models.CharField(max_length=11, blank=True, verbose_name='RG')
    telefone = models.CharField(max_length=14, verbose_name='Telefone')
    tipo_visitante = models.CharField(max_length=20, choices=tipo_visitantes, blank=True, verbose_name='Tipo de Visitante')
    tipo_veiculo = models.CharField(max_length=10, choices=tipo_veiculos, blank=True, verbose_name='Tipo de Veiculo')
    placa = models.CharField(max_length=8, blank=True, verbose_name='Placa')
    modelo = models.CharField(max_length=50, blank=True, verbose_name='Modelo')
    placa_reboque = models.CharField(max_length=8, blank=True, verbose_name='Placa do Reboque')
    cor = models.CharField(max_length=10, blank=True, verbose_name='Cor')
    observacoes = models.TextField(max_length=200, blank=True, verbose_name='Observações')
    objetos = models.CharField(max_length=100, blank=True, verbose_name='Descrição de Objetos')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Portarias'
        verbose_name_plural = 'Portarias'


class Crachas(models.Model):
    visitante = models.ForeignKey(Visitantes, on_delete=models.CASCADE, default=False)
    numero_cracha = models.IntegerField(verbose_name='Número do Crachá')
    entrada = models.DateTimeField(verbose_name='Horário de Entrada')
    saida = models.DateTimeField(verbose_name='Horário de Saída')

    def __str__(self):
        return self.numero_cracha
