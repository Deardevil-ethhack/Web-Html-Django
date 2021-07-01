from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import AddData
import os
import json
# Create your views here.

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'data.json')

with open(file_path,'r') as f:
  context = json.load(f)

def index(request):

    if request.user.is_authenticated:
        context.update({'logout_dis': 'inline-block'})
        context.update({'login_dis': 'none'})
    else:
        context.update({'login_dis': 'inline-block'})
        context.update({'logout_dis': 'none'})
    context.update({'site_title': context['title']})

    return render(request, 'index.html', context)

def handlelogin(request):
  if request.method == 'POST':
      user = request.POST.get('username')
      passw = request.POST.get('password')
      user = authenticate(username=user, password=passw)
      if user is not None:
          login(request, user)
          return redirect("/")
      else:
          messages.error(request, 'You are not a user')
  return redirect("/")


def handlelogout(request):
    logout(request)
    return redirect("/")

def database(request):
  if request.user.is_authenticated:
    context.update({'logout_dis': 'inline-block'})
    context.update({'login_dis': 'none'})
  else:
    context.update({'login_dis': 'inline-block'})
    context.update({'logout_dis': 'none'})

  context.update({'site_title': context['title']+' | Database'})
  context.update({'datas': AddData.objects.all()})
    
  return render(request, 'database.html', context)

def editData(request):

  context.update({'site_title': context['title']+' | Edit Data'})
  if request.user.is_authenticated:
    if request.method == 'POST':
      name = request.POST.get('name')
      place = request.POST.get('place')
      disc = request.POST.get('discription')
      image = request.POST.get('image')
      print(name , place, disc, image)
      data = AddData.objects.create(
        name = name,
        place = place,
        disc = disc,
        image = image
        )
      data.save()
    context.update({'datas': AddData.objects.all()})
    return render(request, 'editData.html', context)
  else:
    return redirect('error')

def deletedata(request,name):
  deldata = AddData.objects.filter(name = name)
  deldata.delete()
  return redirect('editData')

def error(request):
  return render( request, 'error.html')
    
