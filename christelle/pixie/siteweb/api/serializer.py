from rest_framework import serializers
from siteweb import models as models_siteweb

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_siteweb.Banner
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_siteweb.Banner
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_siteweb.About
        fields = '__all__'


class NewslettersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models_siteweb.Newsletters
        fields = '__all__'


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_siteweb.Configuration
        fields = '__all__'


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_siteweb.Website
        fields = '__all__'