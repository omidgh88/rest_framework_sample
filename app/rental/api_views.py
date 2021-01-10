from rest_framework import viewsets
from .models import Friend, Belonging, Borrowed
from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
