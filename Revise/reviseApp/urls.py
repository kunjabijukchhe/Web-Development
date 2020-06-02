from django.conf.urls import url
from reviseApp import views

urlpatterns=[
    url('^$',views.form,name='form')
]
