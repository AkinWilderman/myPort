from django.db import models


class Job(models.Model):
    image = models.ImageField('Job Image', upload_to='images/')
    description = models.TextField('Job Description', max_length=200)
    link = models.URLField('Job Link')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.description
