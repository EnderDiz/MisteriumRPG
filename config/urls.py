from django.urls import path, include

urlpatterns = [
    path('', include('game.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
