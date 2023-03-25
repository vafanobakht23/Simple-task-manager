from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.tasksList, name="tasks"),
    path('',views.taskDetail, name="detail"),
    path('',views.createTask, name="create"),
]
