# Generated by Django 2.1.7 on 2019-07-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='Jumbotron_Text',
            field=models.TextField(max_length=300, verbose_name='Jumbotron Text'),
        ),
        migrations.AlterField(
            model_name='home',
            name='statement',
            field=models.TextField(verbose_name='Statement'),
        ),
    ]