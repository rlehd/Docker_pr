from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_word, name='add_word'),
    path('delete/<int:pk>/', views.delete_word, name='delete_word'), # 삭제 기능 주소
    path('edit/<int:pk>/', views.edit_word, name='edit_word'),# 수정 기능
    path('export/', views.export_csv, name = 'export_csv'),

]
