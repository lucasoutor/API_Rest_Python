# Generated by Django 3.1.1 on 2020-09-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('Emp_cd', models.CharField(max_length=4)),
                ('cpf', models.CharField(max_length=11)),
                ('celular', models.CharField(max_length=12)),
            ],
        ),
    ]
