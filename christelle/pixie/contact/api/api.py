from . import serializer
from contact import models as models_contact
from rest_framework import viewsets


class ContactViewset(viewsets.ModelViewSet):
    queryset = models_contact.Contact.objects.filter(status=True)
    serializer_class = serializer.ContactSerializer