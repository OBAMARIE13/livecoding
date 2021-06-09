from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Produits)
class ProduitsAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'quantite', 'nom', 'prix', 'categorie', 'description', 'chare', 'date_add', 'date_update', 'status')
    list_editable = ['status']

    def view_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
    view_image.short_description = 'Apercu images view_image'




@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = ('nom', 'date_add', 'date_update', 'status')
	list_editable = ['status']