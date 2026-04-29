from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_word, name='add_word'),
    path('delete/<int:pk>/', views.delete_word, name='delete_word'), 
    path('edit/<int:pk>/', views.edit_word, name='edit_word'),
    path('export/', views.export_csv, name = 'export_csv'),

]
