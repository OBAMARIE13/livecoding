from rest_framework import serializers
from contact import models as models_contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_contact.Contact
        fields = '__all__'