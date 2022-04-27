# Generated by Django 3.2.6 on 2021-12-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
                ('date_de_naissance', models.CharField(max_length=120)),
                ('lieu_de_naissance', models.CharField(max_length=120)),
                ('numero_telephone', models.CharField(max_length=120)),
                ('adresse', models.CharField(max_length=120)),
                ('dipomes', models.CharField(max_length=120)),
                ('last_diplome', models.CharField(max_length=120)),
                ('qualification', models.CharField(max_length=120)),
                ('last_job', models.CharField(max_length=120)),
                ('biograpy', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
