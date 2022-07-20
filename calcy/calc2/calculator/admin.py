from django.contrib import admin
from .models.input import Input
# Register your models here.


class AdminInput(admin.ModelAdmin):
    list_display = ['id', 'operand1','operand2','operator', 'result']


#code for registering models.

admin.site.register(Input, AdminInput)
