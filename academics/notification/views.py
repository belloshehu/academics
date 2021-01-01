from django.shortcuts import (
    render,
    reverse,
    get_list_or_404
)

from django.views.generic import DetailView, ListView

from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Notification


class NotificationListView(ListView):
    model = Notification
    template_name = 'notification/notification_list.html'
    context_object_name = 'notifications'


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification/notification_detail.html'


class NotificationUpdateView(UpdateView):
    model  = Notification
    template_name = 'notification/notification_update.html'
    fields = (
        'title',
        'message',
        'degree',
        'target_receiver'
    )

    def get_success_url(self):
        object_id = self.kwargs.get('pk')
        return reverse('notification:notification-detail', kwargs={'pk':object_id})


class NotificationCreateView(CreateView):
    model = Notification
    template_name = 'notification/notification_form.html'
    fields = (
        'title',
        'message',
        'degree',
        'target_receiver'
    )

    def form_valid(self, form, *args, **kwargs):
        form.instance.sender = self.request.user
        return super().form_valid(form, *args, **kwargs)

    def get_success_url(self):
        return reverse('notification:notification-list')


class NotificationDeleteView(DeleteView):
    ''' View to delete an instance of notification.'''
    model = Notification
    template_name = 'notification/notification_delete.html'

    def get_success_url(self):
        return reverse('notification:notification-list')
