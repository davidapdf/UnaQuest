# Generated by Django 3.0.7 on 2020-06-14 07:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=400)),
                ('flegCerto', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=5000)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('aprovado', models.BooleanField(default=False)),
                ('resposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questoes.Resposta')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Professor')),
            ],
        ),
    ]
