from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Listview.as_view(), name='cbvhome'),
    path('details/<int:pk>/', views.Detailsview.as_view(), name='details'),
    path('cbupdate/<int:pk>/', views.Editview.as_view(), name='cbupdate'),
    path('cbdelete/<int:pk>/', views.Delete.as_view(), name='cbdelete')
]
