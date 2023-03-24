from django.urls import path
from game.views.api.login import signin
from game.views.api.logout import signout
from game.views.api.register import register
from game.views.api.get_status import get_status
from game.views.api.index import index,test
from game.views.api.add_score import add_score
urlpatterns = [
    path('',index),
    path('test/',test),
    path('login/',signin),
    path('logout/',signout),
    path('register/',register),
    path('get_status/',get_status),
    path('add_score/',add_score)
]