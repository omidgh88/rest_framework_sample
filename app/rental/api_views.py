from rest_framework import viewsets
from .models import Friend, Belonging, Borrowed
from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner, IsAuthenticatedOrReadOnly, ]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer
    permission_classes = [IsOwner, IsAuthenticatedOrReadOnly, ]


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [IsOwner, IsAuthenticatedOrReadOnly, ]
