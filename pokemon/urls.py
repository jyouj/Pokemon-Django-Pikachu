from django.urls import path

from pokemon import views

app_name = 'pokemon'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]
