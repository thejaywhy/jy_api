import uuid
from django.db import models

class Link(models.Model):
    """
    A model for listing out various Social Media Links related to me
    """
    name = models.TextField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    link_url = models.URLField()
    description = models.TextField()

    class Meta:
        ordering = ('name',)


class Role(models.Model):
    """
    A model for capturing the various roles I have held or would like to hold
    """
    name = models.TextField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)


class Task(models.Model):
    """
    A model for capturing the various tasks I have worked on in the past
    or would like to work on in the future
    """
    name = models.TextField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    role = models.ForeignKey("Role", blank=True, related_name='tasks')

    class Meta:
        ordering = ('name',)


class Interest(models.Model):
    """
    A model for capturing the interests, both personal & professional
    """
    name = models.TextField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    role = models.ForeignKey("Role", blank=True, related_name='interests')


    class Meta:
        ordering = ('name',)
