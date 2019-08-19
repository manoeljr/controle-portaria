# Generated by Django 2.1.1 on 2018-09-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crachas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cracha', models.IntegerField(verbose_name='Número do Crachá')),
                ('entrada', models.DateTimeField(verbose_name='Horário de Entrada')),
                ('saida', models.DateTimeField(verbose_name='Horário de Saída')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('placa_reboque', models.CharField(max_length=8, verbose_name='Placa do Reboque')),
                ('cor', models.CharField(max_length=10, verbose_name='Cor')),
                ('observacoes', models.TextField(max_length=200, verbose_name='Observações')),
                ('objetos', models.CharField(max_length=100, verbose_name='Descrição de Objetos')),
            ],
        ),
        migrations.CreateModel(
            name='Visitantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=11, verbose_name='RG')),
                ('telefone', models.PositiveIntegerField(verbose_name='Telefone')),
            ],
        ),
    ]