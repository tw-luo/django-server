from django.http import JsonResponse

def get_status(request):
    if request.user.is_authenticated:
        response = {'result': 'login','username':request.user.username}
    else:
        response = {'result': 'logout'}
    
    return JsonResponse(response)
