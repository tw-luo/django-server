from game.models.score import Score
from django.utils import timezone
from django.http import JsonResponse

#register
def add_score(request):
    if request.user.is_authenticated:
        score_type="focus"      
        test_score=10
        new_score=Score(user=request.user,test_type=score_type,score=test_score,test_date=timezone.now())
        new_score.save()
    else:
        return JsonResponse({
            'result':'failed',
            'info':"请登录后再使用",
        })
    return JsonResponse({
        'result':'success',
        'type':score_type,
    })
