from django.urls import include, path
from .views import ContactsList, ContactDetail



urlpatterns = [
    path('', ContactsList.as_view()),
    path('<int:pk>/', ContactDetail.as_view())
]
