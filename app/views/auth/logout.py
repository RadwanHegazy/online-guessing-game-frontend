from django.shortcuts import redirect


def LogoutView (request) : 

    response = redirect('login')
    response.delete_cookie('user')
    return response


