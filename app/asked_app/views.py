from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    template = loader.get_template('asked_app/template/index.html')
 #   return HttpResponse(template.render())

def index(request):
    return render(request, 'asked_app/index.html')
