from django.conf.urls import url
from app import views

app_name='app'

urlpatterns=[
    url(r'main/',views.main,name='main'),
    url(r'other/',views.other,name='other'),
]
