from email import message
import re
from threading import local
from django.contrib.auth.forms import PasswordChangeForm
from django.db import models
from django.forms import fields
from django.http import request
from django.shortcuts import redirect, render
from cv.models import Article, cv, profil
from cv.forms import *
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

# page d'acceuil


class home(TemplateView):
    template_name = 'cv/home.html'


"""class CreateCv(LoginRequiredMixin, CreateView):
    model = cv
    fields = '__all__'
    template_name = 'cv/add.html'

    success_message = 'merci'"""


@login_required
def CreateCv(request):

    if request.method == "POST":
        form = cvForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(liste))

    else:
        form = cvForm()

    return render(request, 'cv/add.html', locals())


class ListCv(LoginRequiredMixin, ListView):
    model = cv
    context_object_name = 'cv'
    template_name = 'cv/list.html'
    queryset = cv.objects.order_by('-date')


@login_required(redirect_field_name="/login/")
def liste(request):
    Cv = cv.objects.order_by('-date')

    return render(request, 'cv/list.html',  {'cv': Cv})


class voir(LoginRequiredMixin, DetailView):
    context_object_name = 'cv'
    model = cv
    template_name = 'cv/voir.html'


"""class createprofil(LoginRequiredMixin, CreateView):
    model = profil
    fields = ['site_web', 'avatar', 'signature']
    template_name = 'cv/profil.html'
    success_url = 'list/'"""


@login_required
def createprofil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(liste))
    else:
        form = ProfilForm()
    return render(request, 'cv/profil.html', locals())


@login_required
def monprofil(request):
    Cv = cv.objects.order_by('-date')
    return render(request, 'cv/monprofil.html', {'cv': Cv})


"""def connexion(request):
    error = False

    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'cv/connexion.html', locals())"""


"""def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))"""


class LoginTap(LoginView):
    template_name = 'cv/connexion.html'
    form = ConnexionForm
    next = "/monprofil/"


class LogoutTap(LogoutView):
    next_page = '/login/'
    template_name = 'cv/connexion.html'
    redirect_field_name = "redirection"


class change(PasswordChangeView):
    template_name = "cv/change.html"
    post_change_redirect = '/confirm/'


class changeconfirme(PasswordChangeDoneView):
    template_name = 'cv/confirme.html'


"""class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article

    fields = ['titre', 'contenu', 'image']
    template_name = 'cv/addarticle.html'
    success_url = '/home/'

    success_message = 'merci'"""


@login_required
def CreateArticle(request):
    if request.method == 'POST':
        form = addarticle(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(CreateArticle))
    else:
        form = addarticle()
    return render(request, 'cv/addarticle.html', locals())


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "User has been registred")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
        return redirect(reverse(createprofil))
    else:
        form = UserCreationForm()
    return render(request, 'cv/register.html', locals())
