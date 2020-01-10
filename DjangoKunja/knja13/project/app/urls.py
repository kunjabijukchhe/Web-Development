from django.conf.urls import url

from app import views
app_name='app'
urlpatterns=[
    url(r'one/',views.html,name='html'),
    url(r'two/',views.html1,name='html1'),


]
