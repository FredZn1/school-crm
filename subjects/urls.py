from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path('', views.subject_list, name='list'),
    path('create/', views.subject_create, name='create'),
    path('<int:pk>/', views.subject_detail, name='detail'),
    path('<int:pk>/update/', views.subject_update, name='update'),
    path('<int:pk>/delete/', views.subject_delete, name='delete'),
]
