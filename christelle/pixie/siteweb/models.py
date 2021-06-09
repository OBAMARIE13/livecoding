from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Banner(models.Model):
    titre = models.CharField(max_length=200)
    image = models.FileField(upload_to='image-Site')
    descriptions = HTMLField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.titre


# modelabout
class About(models.Model):
    titre = models.CharField(max_length=200)
    image = models.FileField(upload_to='image-Site')
    descriptions = HTMLField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)



    class Meta():
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.titre


# modelNewsletters
class Newsletters(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = "Newsletters"
        verbose_name_plural = "Newsletterss"

    def __str__(self):
        return self.email

# modelsconfiguration
class Configuration(models.Model):
    copyrights = models.CharField(max_length=200)
    descriptionNewsletters = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)



    class Meta():
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return self.copyrigths

# modelWebSite
class Website(models.Model):
    nom = models.CharField(max_length=200)
    logo = models.FileField(upload_to='image-Site')
    maps = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return self.nom


# modelreseaux
class Reseaux(models.Model):
    nom = models.CharField(max_length=200)
    icone = models.CharField(max_length=200)
    lien = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return self.nom
