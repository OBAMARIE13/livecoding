from . import serializer
from siteweb import models as models_siteweb
from rest_framework import viewsets


class BannerViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.Banner.objects.filter(status=True)
    serializer_class = serializer.BannerSerializer


class AboutViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.About.objects.filter(status=True)
    serializer_class = serializer.AboutSerializer

class NewslettersViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.Newsletters.objects.filter(status=True)
    serializer_class = serializer.NewslettersSerializer


class ConfigurationViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.Configuration.objects.filter(status=True)
    serializer_class = serializer.ConfigurationSerializer

class WebsiteViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.Website.objects.filter(status=True)
    serializer_class = serializer.ConfigurationSerializer


class ReseauxViewset(viewsets.ModelViewSet):
    queryset = models_siteweb.Reseaux.objects.filter(status=True)
    serializer_class = serializer.ConfigurationSerializer

