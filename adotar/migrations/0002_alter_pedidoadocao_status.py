# Generated by Django 5.0.1 on 2024-01-31 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adotar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoadocao',
            name='status',
            field=models.CharField(choices=[('AG', 'Aguardando aprovação'), ('AP', 'Aprovado'), ('R', 'Recusado')], default='AG', max_length=2),
        ),
    ]
