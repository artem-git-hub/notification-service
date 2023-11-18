from django.urls import path
from .views import (
    ClientListCreateView, ClientDetailView,
    DispatchListCreateView, DispatchDetailView,
    MessageListCreateView, MessageDetailView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    
    path('dispatches/', DispatchListCreateView.as_view(), name='dispatch-list-create'),
    path('dispatches/<int:pk>/', DispatchDetailView.as_view(), name='dispatch-detail'),

    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
]