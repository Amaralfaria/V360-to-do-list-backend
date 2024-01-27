from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

class CreateUsuarioView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            #a
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
