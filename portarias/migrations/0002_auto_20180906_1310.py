# Generated by Django 2.1.1 on 2018-09-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portarias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculos',
            name='tipo_veiculo',
            field=models.CharField(blank=True, choices=[('CAMINHÃO', 'Caminhão'), ('CARRETA', 'Carreta'), ('CARRO', 'Carro'), ('MOTO', 'Moto'), ('REBOQUE', 'Reboque')], max_length=10, verbose_name='Tipo de Veiculo'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='tipo_visitante',
            field=models.CharField(blank=True, choices=[('AJUDANTE', 'Ajudante'), ('FUNCIONÁRIO SJK', 'Funcionário SJK'), ('MOTORISTA', 'Motorista'), ('PRESTADOR DE SERVIÇO', 'Prestador de Serviço'), ('VISITANTE', 'Visitante')], max_length=20, verbose_name='Tipo de Visitante'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='veiculo',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='portarias.Veiculos'),
        ),
    ]