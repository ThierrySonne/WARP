# Generated by Django 5.1.2 on 2024-10-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da ONG', max_length=60, verbose_name='Nome')),
                ('cnpj', models.CharField(help_text='CNPJ da ONG', max_length=18, unique=True, verbose_name='Cnpj')),
                ('fone', models.CharField(help_text='Telefone da ONG', max_length=15, verbose_name='Fone')),
                ('ramo', models.CharField(help_text='Ramo de atuação da ONG', max_length=100, verbose_name='Ramo')),
                ('escala', models.CharField(help_text='Escala da ONG', max_length=10, verbose_name='Escala')),
            ],
            options={
                'verbose_name': 'ONG',
                'verbose_name_plural': 'ONGs',
            },
        ),
    ]
