from django.urls import path
from .views import (
    ContactCreateView,
    ContactListView,
    ContactDetailView
)

urlpatterns = [
    # Public contact form
    path(
        '',
        ContactCreateView.as_view(),
        name='contact-create'
    ),
    # Admin list
    path(
        'messages/',
        ContactListView.as_view(),
        name='contact-list'
    ),
    # Single message
    path(
        'messages/<int:pk>/',
        ContactDetailView.as_view(),
        name='contact-detail'
    ),
]