from django.urls import include, path
from .views import ContactsList, ContactDetail, PhoneNumberlist, PhoneNumberDetail



urlpatterns = [
    path('', ContactsList.as_view(), name='contacts-list'),
    path('<int:pk>/', ContactDetail.as_view()),
    path('<int:contact_id>/phoneNumbers', PhoneNumberlist.as_view()),
    path('<int:contact_id>/phoneNumbers/<int:pk>/', PhoneNumberDetail.as_view())

]
