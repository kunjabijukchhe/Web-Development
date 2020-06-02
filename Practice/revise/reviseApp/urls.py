from django.conf.urls import url
from reviseApp import views

urlpatterns=[
    url('',views.users,name="users")
]
