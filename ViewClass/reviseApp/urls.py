from django.urls import path
from django.conf.urls import url,include
from reviseApp import views
app_name='reviseApp'
# urlpatterns = [
#     url(r'^$',views.SchoolViewList.as_view(),name='list'),
#     url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailList.as_view()),
#
# ]
urlpatterns = [
    path('',views.SchoolViewList.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailList.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeteteView.as_view(),name='delete'),
]
