from django.conf.urls import url
from django.urls import path
from reviseApp import views
app_name='reviseApp'
urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
]
