from django.db import models

# Create your models here.
class Produits(models.Model):
    quantite = models.IntegerField(default=False)
    image = models.FileField(upload_to='image_Prestations')
    nom = models.CharField(max_length =200)
    prix = models.IntegerField(default=True)
    categorie = models.ForeignKey('prestations.Categorie', related_name='categorie_fichier', on_delete=models.CASCADE)
    description = models.TextField()
    chare = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = "Produit"
        verbose_name_plural = "produits"

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom
