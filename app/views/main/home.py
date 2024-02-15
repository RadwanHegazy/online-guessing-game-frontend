from django.shortcuts import render
from globals.decorators import login_required

@login_required
def HomeTemplate(request) : 
    context = {}

    return render(request,'home.html',context)