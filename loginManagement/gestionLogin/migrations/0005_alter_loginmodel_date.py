# Generated by Django 5.0.4 on 2024-05-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionLogin', '0004_alter_loginmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='date',
            field=models.DateTimeField(),
        ),
    ]