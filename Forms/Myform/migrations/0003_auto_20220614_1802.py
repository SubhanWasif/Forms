# Generated by Django 3.2.9 on 2022-06-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myform', '0002_remove_formsmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsmodel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='formsmodel',
            name='message',
            field=models.CharField(max_length=255, verbose_name='Messagae'),
        ),
        migrations.AlterField(
            model_name='formsmodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterModelTable(
            name='formsmodel',
            table='informations',
        ),
    ]
