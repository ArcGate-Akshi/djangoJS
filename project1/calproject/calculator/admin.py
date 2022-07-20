from django.contrib import admin
from .models.input import Input
from .models.calcy import Calcy


# Register your models here.
class AdminInput(admin.ModelAdmin):
    list_display = ['id', 'operand1', 'operand2', 'operator', 'result']


class AdminCalcy(admin.ModelAdmin):
    list_display = ['id', 'expression', 'output']

#code for registering models.


admin.site.register(Input, AdminInput)
admin.site.register(Calcy, AdminCalcy)
