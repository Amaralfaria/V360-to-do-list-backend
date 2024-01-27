from rest_framework import serializers
from list.models import (
    List,
    ListItem
)

class ListSerializer(serializers.Serializer):
    class Meta:
        model = List
        fields = '__all__'
        read_only_fields = ['id']

class ListItemSerializer(serializers.Serializer):
    class Meta:
        model = ListItem
        fields = '__all__'
        read_only_fields = ['id']



    