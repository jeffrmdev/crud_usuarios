# Generated by Django 5.0.3 on 2024-03-13 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['-id'], 'verbose_name': 'CRUD Usuario', 'verbose_name_plural': 'CRUD Usuarios'},
        ),
    ]
