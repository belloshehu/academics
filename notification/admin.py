from django.contrib import admin
from .models import (
    Notification,
    IndividualNotification,
    NotificationDegree,
    ReceiverCategory
    )

admin.site.register(Notification)
admin.site.register(NotificationDegree)
admin.site.register(ReceiverCategory)
admin.site.register(IndividualNotification)
