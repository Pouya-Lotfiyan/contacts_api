from .serializers import ContactSerializer, PhoneNumberSerializer
from .models import Contact, PhoneNumber
from rest_framework.response import Response
from rest_framework import generics

class ContactsList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer



class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer


class PhoneNumberlist(generics.ListCreateAPIView):
    lookup_field = 'contact_id'
    queryset = PhoneNumber.objects.all().select_related('contact')
    serializer_class = PhoneNumberSerializer

    def get(self, request, format=None, contact_id=None):
        all = PhoneNumber.objects.filter(contact=contact_id).values()
        return Response(all)


class PhoneNumberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all().select_related('contact')
    serializer_class = PhoneNumberSerializer
