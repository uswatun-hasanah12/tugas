from django.shortcuts import render
from django.http import HttpResponse
from django. template import loader

def website (request):
    template = loader. get_tempate('coding1.html')
    return HttpResponse (template.render())
def index (request):
    template = loader.get_template('coding2.html')  
    return HttpResponse(template.render())

