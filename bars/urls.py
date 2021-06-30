from django.urls import path
from .views import BarList, BarDetail

urlpatterns = [
  path('', BarList.as_view(), name = 'bar_list'),
  path('<int:pk>/', BarDetail.as_view(), name='bar_detail'),
]