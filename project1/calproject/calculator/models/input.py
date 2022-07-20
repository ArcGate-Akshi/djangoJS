from django.db import models


class Input(models.Model):
    operand1 = models.CharField
    operand2 = models.CharField
    operator = models.CharField(max_length=10)
    result = models.CharField
    class Meta:
        db_table = 'input'
