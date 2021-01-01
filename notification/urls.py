from django.urls import path
from .views import (
    NotificationDetailView, 
    NotificationUpdateView,
    NotificationListView,
    NotificationCreateView,
    NotificationDeleteView
) 

app_name = 'notification'
urlpatterns = [
    path(
        'list/',
        NotificationListView.as_view(),
        name='notification-list'

    ),
    path(
        'detail/<int:pk>/',
        NotificationDetailView.as_view(),
        name='notification-detail'
    ),
    path(
        'update/<int:pk>/',
        NotificationUpdateView.as_view(),
        name='notification-update'
    ),
    path(
        'create/',
        NotificationCreateView.as_view(),
        name='notification-create'
    ),
    path(
        'delete/<int:pk>/',
        NotificationDeleteView.as_view(),
        name='notification-delete'
    )
]