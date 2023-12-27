from django.urls import path

from core.views import iris_list

urlpatterns = [
    path('', iris_list, name='iris_list')
]
