from django.conf.urls import url
from app import views


urlpatterns=[
    url(r'^$',views.user,name='user'),

]
