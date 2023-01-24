from django.urls import path

from . import views

urlpatterns = [
    path('start/', views.index, name='index'),
    path('v1/', views.v1, name='view1'),
]


#start/