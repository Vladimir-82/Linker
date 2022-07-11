from django.urls import path
from django.views.generic.edit import View_List
from .views import reduce

urlpatterns = [
    path('', reduce, name='reduce'),
    # path('list', View_List.as_view()),
]