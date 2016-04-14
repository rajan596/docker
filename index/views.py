from django.shortcuts import render
from django.http import HttpResponse
from .models import document
from django.shortcuts import render
from django.template import loader
from django.http import Http404

# Create your views here.

def home(request):
    return render(request,"index/index.html")
    """
    docs=document.objects.all()
    template=loader.get_template("index/index.html")
    context={
        "docs":docs,
    }
    return HttpResponse(template.render(context,request))
    """

def view_document(request,pk):
    doc=document.objects.get(pk=pk)

    if doc:
        template=loader.get_template("index/document.html")
        context={
            "doc":doc,
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("Not found")
