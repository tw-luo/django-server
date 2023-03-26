from django.http import JsonResponse

def get_status(request):
    if request.user.is_authenticated:
        is_super = request.user.is_superuser
        response = {'result': 'login','username': request.user.username, 'is_super': is_super}
    else:
        response = {'result': 'logout'}
    
    return JsonResponse(response)
