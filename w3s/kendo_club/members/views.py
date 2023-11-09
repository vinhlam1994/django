from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member,Level

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers
    }

    return HttpResponse(template.render(context,request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    memberLevel = Level.objects.get(pk=id)

    template = loader.get_template('details.html')
    context = {
        'mymember':mymembers,
        'memberLevel':memberLevel,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
        'x': ['Apple', 'Banana', 'Cherry'], 
        'y': ['Apple', 'Banana', 'Cherry'], 
    }
    return HttpResponse(template.render(context, request))