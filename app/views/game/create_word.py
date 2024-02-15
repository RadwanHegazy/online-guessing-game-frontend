from django.shortcuts import render
from globals.decorators import login_required
from django.http import JsonResponse
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@login_required
def CreateBattle(request) : 
    context = {}

    if request.method == "POST" : 
        word = request.POST.get('word',None)
        help_text = request.POST.getlist('help_text')

        user_token = request.COOKIES.get('user')

        
        data = {
            'help_text' : help_text,
            'word' : word
        }


        

        action = Action(
            url = MAIN_URL + "/battle/create/",
            headers={"Authorization":f"Bearer {user_token}"},
            data = data
        )
        
        action.post()
        
        return JsonResponse(action.json_data(),safe=False)


    return render(request,'create-word.html',context)