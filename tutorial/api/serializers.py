from django.contrib.auth.models import User, Group
from tutorial.api.models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('classification', 'ip_address')
