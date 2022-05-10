from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http.response import HttpResponse, HttpResponseRedirect
from matplotlib.backend_bases import RendererBase
from .models import applists
from datetime import datetime
from django.utils import formats

def addapp(request):
    applis= applists()
    if request.method=='POST':
        app_name = request.POST.get('app_name')
        app_im= request.FILES.get('app_im')
        last_date= datetime.now()

        applis.appname=app_name
        applis.appimg= app_im
        applis.updated_at=last_date
        applis.save()
        return redirect('showapps')
    else:
        return render(request, 'applist.html')

def showapps(request):
    appli=applists.objects.all()
    return render(request,'showapps.html',{'showapp':appli})

def deleteapp(request,appname):
    deli=applists.objects.get(appname=appname)
    deli.delete()
    return redirect('showapps')
