from django.urls import path
from . import views


app_name='blog'

urlpatterns=[
    path('post/',views.new_post_view,name='new_post_view'),
]