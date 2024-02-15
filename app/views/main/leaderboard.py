from django.shortcuts import render
from globals.decorators import login_required
from frontend.settings import MAIN_URL
from globals.request_manager import Action

@login_required
def LeaderBoardTemplate (request) : 

    context = {}

    user_token = request.COOKIES.get('user')
    
    action = Action(
        url = MAIN_URL + "/user/leaderboard/",
        headers={"Authorization":f"Bearer {user_token}"}
    )

    action.get()

    context['leaders'] = action.json_data()


    return render(request,'leaderboard.html',context)