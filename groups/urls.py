from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.group_list, name='list'),
    path('create/', views.group_create, name='create'),
    path('<int:pk>/', views.group_detail, name='detail'),
    path('<int:pk>/update/', views.group_update, name='update'),
    path('<int:pk>/delete/', views.group_delete, name='delete'),
]
