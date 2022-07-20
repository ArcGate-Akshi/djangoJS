from django.shortcuts import render
from .models import input

# Create your views here.
def index(request):
    return render(request, 'index.html')


def admin(request):
    return render(request, 'index.html')

def getdata(request):

            # request.POST.get('first') and request.POST.get('second') and request.POST.get('result'):
            post=input()
            post.operand1=request.POST.get('first')
            post.operand2 = request.POST.get('second')
            post.result = request.POST.get('result')
            post.save()
            return render(request, 'create.html')


