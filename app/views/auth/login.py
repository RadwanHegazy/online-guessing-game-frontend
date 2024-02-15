from django.shortcuts import redirect, render
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def LoginTemplate (request) : 
    context = {}
    
    if request.method == "POST" : 
        data = {
            'email' : request.POST.get('email',None),
            'password' : request.POST.get('password',None)
        }

        user = Action(
            url = MAIN_URL + "/user/login/",
            data = data
        )

        user.post()

        if user.is_valid() : 
            response = redirect('home')
            response.set_cookie('user',user.json_data()['access'])
            return response
        
        context['error'] = "البيانات غير صحيحة"

    return render(request,'login.html',context)


