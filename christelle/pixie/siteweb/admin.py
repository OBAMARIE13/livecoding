from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('view_image', 'titre', 'descriptions', 'date_add', 'date_update', 'status')
	list_editable = ['status']

	def view_image(self, obj):
		return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
	view_image.short_description = 'Apercu images view_image'


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ('view_image', 'titre', 'descriptions', 'date_add', 'date_update', 'status')
	list_editable = ['status']

	def view_image(self, obj):
		return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
	view_image.short_description = 'Apercu images view_image'


@admin.register(models.Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
	list_display = ('email', 'date_add', 'date_update', 'status')
	list_editable = ['status']



@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
	list_display = ('copyrights', 'descriptionNewsletters', 'date_add', 'date_update', 'status')
	list_editable = ['status']


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'nom', 'maps', 'date_add', 'date_update', 'status')
    list_editable = ['status']

    def view_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:130px">')
    view_image.short_description = 'Apercu images view_image'



@admin.register(models.Reseaux)
class ReseauxAdmin(admin.ModelAdmin):
	list_display = ('nom', 'icone', 'lien', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
