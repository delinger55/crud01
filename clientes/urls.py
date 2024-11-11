from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('created/', views.cliente_create, name='cliente_create'),
    path('<int:id>/', views.cliente_detail, name='cliente_detail'),
    path('<int:id>/update/', views.cliente_update, name='cliente_update'),
    path('<int:id>/delete/', views.cliente_delete, name='cliente_delete'),

]
