from django.conf.urls import url
from app import views


app_name='app1'
# app_name='app'

# urlpatterns=[
#     url(r'main/',views.main,name='main'),
#     url(r'other/',views.other,name='other'),
# ]
urlpatterns=[
    url(r'register',views.register,name='register'),
    # url(r'other/',views.other,name='other'),
]
