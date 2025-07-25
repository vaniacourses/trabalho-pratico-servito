# Generated by Django 5.2.4 on 2025-07-07 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField(null=True, verbose_name='Preço')),
                ('prazo', models.DateField(null=True)),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
                ('contratante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='possivel_contratante', to='usuarios.usuario')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='possivel_prestador', to='usuarios.usuario')),
            ],
        ),
    ]
