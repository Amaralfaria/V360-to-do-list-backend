from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout

from user.models import User
from list.models import List
from user.serializers import UserSerializer

class CreateUsuarioView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post','get']

    def test_auth(self,request):
        print(List.objects.get(list_name="teste post").__dict__)
        user = request.user
        print(user)
        return Response(status=status.HTTP_201_CREATED)
    
    def logout_user(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
        


    def login(self,request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        print('Passados',email,password)

        user = User.objects.get(email=email)

        if user is None:
            return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)
        
        
        print(user)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            
            return JsonResponse({
                "refresh":str(refresh),
                "access":str(refresh.access_token),
            })
        else:
            return Response('Wrong password', status=status.HTTP_401_UNAUTHORIZED) 






        
