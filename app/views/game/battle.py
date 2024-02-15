from django.shortcuts import render
from globals.decorators import login_required
from django.http import JsonResponse, Http404
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.views.decorators.csrf import csrf_exempt

@login_required
def Battle(request, battle_id) : 
    context = {}




    user_token = request.COOKIES.get('user')

    action = Action(
        url = MAIN_URL + f"/battle/get/{battle_id}/",
        headers = {"Authorization":f"Bearer {user_token}"}
    )
    
    action.get()
    
    context['data'] = action.json_data()

    if not action.is_valid() : 
        raise Http404(request)
    

    if request.method == "POST" : 
        data = {
            'word' : request.POST['word'],
        }

        action = Action(
            url = MAIN_URL + f"/battle/check/{battle_id}/",
            headers = {"Authorization":f"Bearer {user_token}"},
            data = data,
        )

        action.post()

        status = None
        res = action.json_data()

        if 'correct' in res['message'] : 
            status = 'correct'
        else:
            status = 'wrong'
        context['status'] = status

    return render(request,'battle.html',context)