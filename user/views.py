from rest_framework import viewsets

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
