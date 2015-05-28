from django.db import models
from django.contrib import admin

from jy_api.apps.api.models import (
    Link,
    Role,
    Task,
    Interest
)


class RoleAdmin(admin.ModelAdmin):
    """
    How to display the Role object in the Admin UI
    """
    list_display = ('name', )


class LinkAdmin(admin.ModelAdmin):
    """
    How to display the Link object in the Admin UI
    """
    list_display = ('name', 'link_url', )


class TaskAdmin(admin.ModelAdmin):
    """
    How to display the Task object in the Admin UI
    """
    list_display = ('name', )


class InterestAdmin(admin.ModelAdmin):
    """
    How to display the Interest object in the Admin UI
    """
    list_display = ('name', )


# Register your models here.
admin.site.register(Link, LinkAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Interest, InterestAdmin)
