# Generated by Django 3.0.7 on 2020-06-13 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('questoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questoes', models.ManyToManyField(to='questoes.Questao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Professor')),
            ],
        ),
    ]
