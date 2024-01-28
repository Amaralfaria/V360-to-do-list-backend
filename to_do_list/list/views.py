from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from list.models import List, ListItem
from list.serializers import ListSerializer, ListItemSerializer

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
    
    def put(self,request,list_id):
        try:
            user_list = List.objects.get(user=request.user,id=list_id)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListSerializer(user_list,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,list_id):
        try:
            user_list = List.objects.get(user=request.user,id=list_id)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListItemViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['post']

    def get_user_list_items(self, request,list_id):
        list_items = ListItem.objects.filter(list__user=request.user,list_id=list_id)
        serializer = ListItemSerializer(list_items,many=True)

        return JsonResponse({
            "list_items":serializer.data
        }, status=status.HTTP_200_OK)
    
    def get_item(self,request,item_id):
        try:
            list_item = ListItem.objects.get(list__user=request.user,id=item_id)
        except ListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        serializer = ListItemSerializer(list_item)
        return Response(serializer.data)
    
    def put(self,request,item_id):
        try:
            list_item = ListItem.objects.get(list__user=request.user,id=item_id)
        except ListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListItemSerializer(list_item,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,item_id):
        try:
            list_item = ListItem.objects.get(list__user=request.user,id=item_id)
        except ListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        list_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        

        






    
     