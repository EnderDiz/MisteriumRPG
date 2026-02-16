from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('observer/', views.observer, name='observer'),

    path('guide/', views.guide, name='guide'),
    path('patchnote/', views.patchnote, name='patchnote'),
    path("login/", views.login_view, name="login"),
    path("login/", views.login_view, name="register"),
]
