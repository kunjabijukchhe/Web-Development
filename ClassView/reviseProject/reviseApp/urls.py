from django.conf.urls import url
from reviseApp import views
from django.urls import path

app_name='reviseApp'
# urlpatterns = [
#     url(r'^$',views.SchoolListView.as_view(),name='list'),
#     url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
#     url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
#     url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
#     url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
# ]
urlpatterns = [
    path(r'^$',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
]
