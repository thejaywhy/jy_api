from rest_framework import viewsets

from jy_api.apps.api.models import (
    Link,
    Role,
    Task,
    Interest
)
from jy_api.apps.api.serializers import (
    LinkSerializer,
    RoleSerializer,
    TaskSerializer,
    InterestSerializer
)


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Each link points to info related to me on the Internet.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    There are many Roles I have in my life. Use this API to get a list of them. Always a work in progress.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A Task is something I have worked on, or would like to work on. It's associated with 1 or more roles.

    Use this API to get access to planned Tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class InterestViewSet(viewsets.ReadOnlyModelViewSet):
    """
    An Interest is something I enjoy.

    Use this API to get access to some of my many Interests.
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
