from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def RegisterTemplate (request) : 
    
    context = {}

    if request.method == "POST" : 
        data = {
            "full_name" : request.POST.get('full_name',None),
            "email" : request.POST.get('email',None),
            "password" : request.POST.get('password',None),
        }


        user = Action(
            url = MAIN_URL + "/user/register/",
            data = data,
        )

        if request.FILES : 
            picture = request.FILES['picture']
            user.files = {
                'picture' : picture
            }
        
        user.post()

        if user.is_valid() : 
            response = redirect('home')
            response.set_cookie('user',user.json_data()['access'])
            return response
        
        context['error'] = 'البيانات غير صحيحة'

    return render(request,'register.html',context)


