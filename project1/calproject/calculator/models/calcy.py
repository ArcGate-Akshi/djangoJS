from django.db import models


class Calcy(models.Model):
    expression = models.CharField(max_length=300, default='empty')
    output = models.CharField(max_length=100)

    class Meta:
        db_table = 'calcy'

