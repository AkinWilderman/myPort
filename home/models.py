from django.db import models


class Home(models.Model):
    jumbotron_text = models.TextField('Jumbotron Text', max_length=300)
    statement = models.TextField('Statement')
    company_name = models.CharField('Company Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    state = models.CharField('State', max_length=20)
    postal = models.CharField('Postal Code', max_length=10)
    country = models.CharField('Country', max_length=30)
    keywords = models.CharField('Keywords', max_length=400)
    meta_description = models.TextField('Meta Description', max_length=160)

