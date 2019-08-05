from django.urls import path

from .views import class_list, add_subject

urlpatterns = [
    path('class-list', class_list, name='class-list'),
    path('add-subject/<class_id>', add_subject, name='add-subject')
]