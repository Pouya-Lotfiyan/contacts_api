from .serializers import ContactSerializer
from .models import Contact
from rest_framework import generics

class ContactsList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer
