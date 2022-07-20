import random
from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import input
from .models.calcy import Calcy
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.
def structure(request):
    return render(request, 'structure.html')


def adminPanel(request):
    # get data from db
    value = Calcy.objects.all()
    #field with sessions
    Admins = serializers.serialize('json',User.objects.filter(is_superuser=True))
    onlyUsers = serializers.serialize('json', User.objects.filter(is_superuser=False))
    request.session['Admins'] = Admins
    request.session['only_users'] = onlyUsers

    #cookies showing total days of visits
    visits = int(request.COOKIES.get('visits','0'))

    response = HttpResponse(render, 'adminPanel.html',{'value': value})




def addCalcy(request):

    value = Calcy.objects.get(pk=id)
    if request.method == 'POST':
        expression = request.POST['expression']
        output = request.POST['output']
        insert = Calcy(expression=expression, output=output)
        insert.save()

    return HttpResponseRedirect(reverse('showValues', args=(value.id)))


def showValues(request, id):
    print('sessions: ')
    value = Calcy.objects.get(pk=id)
    calcy = Calcy.objects.filter(value=value)
    return render(request, 'datatable.html', {'value': value, 'calcy': Calcy})


def addValue(request):
     expression = request.POST.get['expression']
     operator = request.POST.get['operator']
     username = request.POST['username']
     email = request.POST['email']
     isAdmin = request.POST.get('isAdmin') == 'on'
     user = User.objects.create_user(username, email, 'Arcgate1!')
     user.is_superuser = isAdmin
     user.expression = expression
     user.operator = operator
     user.save()

     # employee = Employee(user=user, empid=empid)
     # employee.save()

     return HttpResponseRedirect(reverse('adminPanel'))


def calculate(request):
    user_input = input(first=request.POST.get('expression'), second=request.POST.get('operator'))
    user_input.save()
    str1 = "Data inserted to Input table with id: " + str(input.id)
    return render(request, 'structure.html', {'msg': str1})


class sessionBase:
    #base class for all session class
    TEST_COOKIE_NAME = 'testcookie'
    TEST_COOKIE_VALUE = random.randint(1, 1000)

    def setcookie(request):
        html = HttpResponse("<h1> welcome </h1>")
        unique = random.randint(1, 1000)
        html.set_cookie('testcookie', unique,)
        request.session.set_expiry(0)
        return html
    