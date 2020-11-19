from rest_framework import serializers
from PGamersApp.models import *
from django.contrib.auth.models import User, Group

class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']