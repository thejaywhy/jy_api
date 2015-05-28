from rest_framework import serializers
from jy_api.apps.api.models import (
    Link,
    Role,
    Task,
    Interest
)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'name', 'link_url', 'description', 'created', 'url')

class TaskSerializer(serializers.ModelSerializer):
    role = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='role-detail'
    )

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'role', 'created', 'url')


class InterestSerializer(serializers.ModelSerializer):
    role = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='role-detail'
    )

    class Meta:
        model = Interest
        fields = ('id', 'name', 'description', 'role', 'created', 'url')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'tasks', 'interests', 'created', 'url')
