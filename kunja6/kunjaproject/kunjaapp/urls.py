from django.conf.urls import url
from kunjaapp import views

urlpatterns=[
    url(r'^$',views.users,name="index1"),
]
