# Generated by Django 2.1.1 on 2018-09-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portarias', '0003_auto_20180906_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='crachas',
            name='visitante',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='portarias.Visitantes'),
        ),
    ]
