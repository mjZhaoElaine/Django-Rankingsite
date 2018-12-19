from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('times', views.index, name='index'),
    path('cwur', views.cwur, name='cwur'),
    path('shanghai', views.shanghai, name='shanghai'),
]
