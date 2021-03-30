from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/mark_read/<int:message_id>', views.mark_read),
    path('api/get_messages/', views.get_messages),
]
