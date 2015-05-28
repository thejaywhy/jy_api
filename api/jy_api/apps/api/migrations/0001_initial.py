# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('link_url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('role', models.ForeignKey(related_name='tasks', blank=True, to='api.Role')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='interest',
            name='role',
            field=models.ForeignKey(related_name='interests', blank=True, to='api.Role'),
        ),
    ]
