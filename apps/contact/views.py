from rest_framework import generics
from .models import ContactMessage
from .serializers import ContactMessageSerializer

# Public contact form (POST only)
class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

# Admin view (GET messages)
class ContactListView(generics.ListAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

# Single message detail
class ContactDetailView(generics.RetrieveUpdateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer