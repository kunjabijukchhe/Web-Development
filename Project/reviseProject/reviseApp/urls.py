from django.conf.urls import url
from reviseApp import views
app_name='reviseApp'
urlpatterns=[
    url(r'^$',views.user_login,name='user_login'),
    url(r'form/',views.form,name='form')
]
