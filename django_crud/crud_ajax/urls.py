from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
path('',views.account),
path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
]