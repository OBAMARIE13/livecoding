from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom