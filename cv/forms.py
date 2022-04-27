from cProfile import label
from django import forms
from django.forms import fields
from cv.models import cv, profil, Article


class cvForm(forms.ModelForm):
    class Meta:
        model = cv
        fields = '__all__'
        exclude = ('user',)


class ProfilForm(forms.ModelForm):
    class Meta:
        model = profil
        fields = '__all__'
        exclude = ('user',)
        


"""class addform(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    date_de_naissance = forms.CharField()
    lieu_de_naissance = forms.CharField()
    numero_telephone = forms.CharField()
    adresse = forms.CharField()
    dipomes = forms.CharField()
    last_diplome = forms.CharField()
    qualification = forms.CharField()
    experience = forms.IntegerField()
    last_job = forms.CharField()
    biograpy = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()"""


class ConnexionForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisation', max_length=60)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)


"""class addarticle(forms.Form):
    titre = forms.CharField(label='titre')
    contenu = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()"""


class addarticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('user',)
