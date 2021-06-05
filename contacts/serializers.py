

from rest_framework import serializers
from .models import Contact, PhoneNumber




class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('id', 'type', 'number', 'contact')

class ContactSerializer(serializers.ModelSerializer):

    phoneNumbers = PhoneNumberSerializer(many=True)

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'phoneNumbers')
