# Generated by Django 5.2 on 2025-04-10 13:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BichoEstimacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('raca', models.CharField(choices=[('COR', 'Coruja'), ('GATO', 'Gato'), ('LION', 'Leão'), ('RAT', 'Rato')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PersonagensHarryPotter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('casa', models.CharField(choices=[('GRI', 'Grifinoria'), ('SON', 'Sonserina'), ('LUF', 'Lufa-Lufa'), ('COR', 'Corvinal')], max_length=25)),
                ('CPF', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='O CPF do bruxo deve ser no formato XXX.XXX.XXX-XX', regex='^\\d{3}.\\d{3}.\\d{3}-\\d{2}$')])),
                ('qnt_de_nariz', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField()),
                ('patronomo', models.CharField(blank=True, max_length=255, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bichoestimacao')),
            ],
        ),
    ]
