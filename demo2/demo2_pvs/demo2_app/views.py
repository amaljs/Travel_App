from django.shortcuts import render
from .models import  Place,Team
# Create your views here.
def index(requst):
    obj=Place.objects.all()
    obj2=Team.objects.all()

    return  render(requst,'index.html',{'value':obj,'value2':obj2})
def sult(requst):
    num1=int(requst.GET['num1'])
    num2=int(requst.GET['num2'])
    a=num1+num2
    b=num1-num2
    c=num1*num2
    d=num1/num2
    return  render(requst,'result.html',{"add":a,'sub':b,'mul':c,'div':d})