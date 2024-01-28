from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from list.models import List
from list.serializers import ListSerializer

class ListViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['post']

    def get_user_lists(self, request):
        lists = List.objects.filter(user=request.user)
        serializer = ListSerializer(lists,many=True)

        return JsonResponse({
            "lists":serializer.data
        }, status=status.HTTP_200_OK)
    
    def get_user_list(self,request,list_id):
        try:
            user_list = List.objects.get(user=request.user,id=list_id)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        serializer = ListSerializer(user_list)
        return Response(serializer.data)




    
     