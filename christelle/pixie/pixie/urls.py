"""pixie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from siteweb.api import api as siteweb_api
from contact.api import api as contact_api
# from prestations.api import api as prestations_api



router = routers.DefaultRouter()

router.register('siteweb/Banner', siteweb_api.BannerViewset, basename='api-Banner')
router.register('siteweb/About', siteweb_api.AboutViewset, basename='api-about')
router.register('siteweb/Newsletters', siteweb_api.NewslettersViewset, basename='api-Newsletters')
router.register('siteweb/Configuration', siteweb_api.ConfigurationViewset, basename='api-Configuration')
router.register('siteweb/Reseaux', siteweb_api.ReseauxViewset, basename='api-Reseaux')


router.register('contact/Contact', contact_api.ContactViewset, basename='api-Contact')
# router.register('prestations/Produits', prestations_api.ProduitsViewset, basename='api-Produits')
# router.register('prestations/Categorie',prestations_api.CategorieViewset, basename='api-Categorie')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('', include('siteweb.urls')),
    path('api/', include(router.urls)),
]