# Generated by Django 4.1.1 on 2022-09-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
