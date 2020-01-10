from django.urls import path
from appform import views

urlpatterns=[
    path(r'', views.index, name="index"),
    path(r'form/', views.form_name, name="form_name"),
]
