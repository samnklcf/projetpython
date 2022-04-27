from email.policy import default
from operator import truediv
from pyexpat import model
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.


class cv(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    date_de_naissance = models.CharField(max_length=120)
    lieu_de_naissance = models.CharField(max_length=120)
    numero_telephone = models.CharField(max_length=120)
    adresse = models.CharField(max_length=120)
    dipomes = models.CharField(max_length=120)
    last_diplome = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    experience = models.PositiveIntegerField(null=True)
    last_job = models.CharField(max_length=120)
    biograpy = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='date de création')
    photo = models.ImageField(blank=True, upload_to='photo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    site_web = models.URLField(null=True)
    avatar = models.ImageField(
        blank=True, upload_to="img", default='WhatsApp_Image_2020-12-29_at_10.53.46.jpeg')
    signature = models.CharField(max_length=60)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)

    class Meta:
        permissions = (
            ("commenter_article", "commenter article"),
            ("maeque_lu", "Marquer comme lu"),
        )


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    image = models.ImageField(blank=True, null=True,
                              upload_to='article_image/')

    def __str__(self):
        return '{0} par {1}'.format(self.titre, self.user.username)
