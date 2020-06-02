from django.conf.urls import url
from reviseApp import views
app_name='reviseApp'
urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
]
