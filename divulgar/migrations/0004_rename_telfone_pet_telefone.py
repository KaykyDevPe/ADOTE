# Generated by Django 5.0.1 on 2024-01-28 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0003_pet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='telfone',
            new_name='telefone',
        ),
    ]
