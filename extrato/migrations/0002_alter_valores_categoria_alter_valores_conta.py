# Generated by Django 4.2.5 on 2023-09-16 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_conta_banco'),
        ('extrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.categoria'),
        ),
        migrations.AlterField(
            model_name='valores',
            name='conta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.conta'),
        ),
    ]
