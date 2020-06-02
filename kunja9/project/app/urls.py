from django.urls import path
from django.conf.urls import url

from app import views
urlpatterns=[
    path('',views.index,name='index'),
    path('form/',views.users,name='users'),
    # url(r'',views.index,name='index'),
    # url(r'form/',views.users,name='users'),
]
