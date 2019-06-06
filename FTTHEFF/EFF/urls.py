from django.urls import path
from django.conf.urls import url
from EFF import views

app_name = 'EFF'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    url(r'^employees/$',views.EmployeeListView.as_view(),name='employees'),
]