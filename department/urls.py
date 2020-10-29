from django.urls import path
from . import views


app_name = 'department'
urlpatterns = [
    path(
        'list/',
        views.DepartmentListView.as_view(),
        name='department-list'
    ),
    path(
        'detail/<int:pk>',
        views.DepartmentDetailView.as_view(),
        name='detail'
    )
]