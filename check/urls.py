from django.urls import path

from . import views

urlpatterns = [
    path('', views.query, name='index'),
    path('query', views.query, ),
    path('thanks', views.thanks, ),
]

