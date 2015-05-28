# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_link(apps, link={}):
    """
    Create a new instance of the Link object
    """
    Link = apps.get_model("api", "Link")

    new_link = Link.objects.create(
        name=link["name"],
        link_url=link["link_url"],
        description=link["description"]
    )
    new_link.save()


def add_links(apps, schema_editor):
    """
    Initial Dataset for the "Link" resource.
    """

    my_links = {
        "Blog": {
            "name": "Blog",
            "link_url": "http://randomjy.com/",
            "description": "My blog where I write about books mostly. And some tough problems I've had while coding. A new work in progress.",
        },
        "Github": {
            "name": "Github",
            "link_url": "https://github.com/thejaywhy/",
            "description": "My public Github account with repo's I've worked on. ",
        },
        "LinkedIn": {
            "name": "LinkedIn",
            "link_url": "https://www.linkedin.com/in/jonryoung",
            "description": "My LinkedIn Profile",
        },
        "Twitter": {
            "name": "Twitter",
            "link_url": "https://twitter.com/random_jyoung",
            "description": "My Twitter Account!",
        }
    }

    for link in my_links:
        add_link(apps, my_links[link])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_links),
    ]
