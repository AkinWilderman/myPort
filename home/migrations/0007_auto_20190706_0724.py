# Generated by Django 2.1.7 on 2019-07-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190706_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='postal',
            field=models.CharField(max_length=10, verbose_name='Postal Code'),
        ),
    ]