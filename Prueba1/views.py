from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
    ahora = datetime.now().strftime("%D")
    misDatos = {"dia" : ahora} 
    return render(request, "index.html", misDatos)

def whoAmI(request):
    ahora = datetime.now().strftime("%D")
    misDatos = {"dia" : ahora} 
    return render(request, "whoami.html", misDatos)

def menu(request):
    ahora = datetime.now().strftime("%D")
    misDatos = {"dia" : ahora} 
    return render(request, "menu.html", misDatos)

def Pedido(request):
    ahora = datetime.now().strftime("%D")
    misDatos = {"dia" : ahora} 
    return render(request, "contactus.html", misDatos)