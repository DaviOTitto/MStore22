# Generated by Django 4.1 on 2024-06-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_rename_cliente_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='sexo_cli',
            field=models.CharField(choices=[('M', 'option 1 '), ('F', 'option 2 ')], default=1, max_length=1, verbose_name='sexo'),
            preserve_default=False,
        ),
    ]