from os import name
from django.contrib import admin
from django.urls import path, re_path
from cv.views import *

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('add/', CreateCv, name='add'),
    path('add/list/', ListCv.as_view(), name='list'),
    path('voir/<int:pk>/', voir.as_view(), name='voir'),
    path('profil/', createprofil, name='profil'),
    #path('connexion/', connexion, name="connexion"),
    #path('deconnexion/', deconnexion, name='deconnexion'),
    path('liste/', liste, name='liste'),
    path('login/', LoginTap.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutTap.as_view(), name='logout'),
    path('changer/', change.as_view(), name='change'),
    path('confirm/', changeconfirme.as_view(), name='confirm'),
    path('addarticle', CreateArticle, name='addarticle'),
    path('monprofil/', monprofil, name='monprofil'),
    path('register/', register, name='register')

]
