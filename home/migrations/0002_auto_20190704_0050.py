# Generated by Django 2.1.7 on 2019-07-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='postal',
            field=models.IntegerField(),
        ),
    ]