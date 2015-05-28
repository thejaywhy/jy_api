# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_role(apps, role={}):
    """
    Create a new instance of the Role object
    """
    Role = apps.get_model("api", "Role")

    new_role = Role.objects.create(
        name=role["name"],
        description=role["description"]
    )
    new_role.save()


def add_roles(apps, schema_editor):
    """
    Initial Dataset for the "Role" resource.
    """

    my_roles = {
        "Adventurer": {
            "name": "Adventurer",
            "description": "Exploring the world in which we live, and sharing it all with my family.",
        },
        "Assistant-Director-of-Childhood-Experience": {
            "name": "Assistant-Director-of-Childhood-Experience",
            "description": "\"Working\" with my awesome wife to raise two amazing kids!",
        },
        "Backend-Developer": {
            "name": "Backend-Developer",
            "description": "Working with the team to create a delightful user experience for scalable APIs. ",
        },
        "Happiness-Hero": {
            "name": "Happiness-Hero",
            "description": "Just because I'm a developer doesn't mean I can't help users directly!",
        },
        "Lifelong-Learner": {
            "name": "Lifelong-Learner",
            "description": "Never stop learning! There's always room to grow. ",
        },
        "Reliability-Developer": {
            "name": "Reliability-Developer",
            "description": "Building development, test, integration & production environments that are easy to reproduce. Utilizing a continuous delivery pipeline to make deployments simple and reliable.",
        }
    }

    for role in my_roles:
        add_role(apps, my_roles[role])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_add_links'),
    ]

    operations = [
        migrations.RunPython(add_roles),
    ]
