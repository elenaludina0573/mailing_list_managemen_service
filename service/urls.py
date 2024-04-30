from django.urls import path
from service.apps import ServiceConfig
from service.views import (ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
                           ClientDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView,
                           MessageDeleteView)


app_name = ServiceConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('service/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('service/create/', ClientCreateView.as_view(), name='client_from'),
    path('service/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('service/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('service/', MessageListView.as_view(), name='message_list'),
    path('service/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('service/create/', MessageCreateView.as_view(), name='message_from'),
    path('service/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('service/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
