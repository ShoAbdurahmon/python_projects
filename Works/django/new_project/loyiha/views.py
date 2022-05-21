from django.shortcuts import render
from django.http import HttpResponse

def korsat(request):
	return render("Bu Bizning Bosh Sahifamiz !")

def boshSahifa(request):
	return HttpResponse(request,"loyiha/home.html")
