from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BarSerializer
from .models import Bar
from .permissions import IsAuthorOrReadOnly

class BarList(ListCreateAPIView):
  queryset = Bar.objects.all()
  serializer_class = BarSerializer

class BarDetail(RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorOrReadOnly, )
  queryset = Bar.objects.all()
  serializer_class = BarSerializer
