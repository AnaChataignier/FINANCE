# Generated by Django 4.2.5 on 2023-09-17 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_conta_banco'),
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapaga',
            name='conta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.contapagar'),
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.categoria'),
        ),
    ]