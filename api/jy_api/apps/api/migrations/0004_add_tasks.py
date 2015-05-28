# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_task(apps, task={}):
    """
    Create a new instance of the Task object
    """
    Task = apps.get_model("api", "Task")

    new_task = Task.objects.create(
        name=task["name"],
        description=task["description"],
        role=task["role"]
    )
    new_task.save()


def add_tasks(apps, schema_editor):
    """
    Initial Dataset for the "Task" resource.
    """

    Role = apps.get_model("api", "Role")

    adventurer_role = Role.objects.get(name="Adventurer")
    asst_dir_role = Role.objects.get(name="Assistant-Director-of-Childhood-Experience")
    backend_dev_role = Role.objects.get(name="Backend-Developer")
    happiness_role = Role.objects.get(name="Happiness-Hero")
    learner_role = Role.objects.get(name="Lifelong-Learner")
    reliability_dev_role = Role.objects.get(name="Reliability-Developer")

    my_tasks = {
        "Caching": {
            "name": "Caching",
            "description": "Cache all the things! Caching really shouldn't be an after thought. Caching at the client is the most effective, but HTTP caching (ala Varnish), and application level caching to avoid database I/O are important too.",
            "role": reliability_dev_role
        },
        "Configuration-Management": {
            "name": "Configuration-Management",
            "description": "Research currently deployed configuration management tools. If none, compile & recommend list of options.",
            "role": reliability_dev_role
        },
        "Document-Infrastructure": {
            "name": "Document-Infrastructure",
            "description": "Read any existing documentation, and update it to match currently deployed systems.",
            "role": reliability_dev_role
        },
        "Interactive-API-Docs": {
            "name": "Interactive-API-Docs",
            "description": "Interactive API docs, IMO lead to a delightful developer experience. A browsable API is a great start. But interactive UIs are even better. For example, swagger.io or apiary.io provide a simple way for developers to test out APIs without having to write any code.",
            "role": backend_dev_role
        },
        "NGINX+Lua": {
            "name": "NGINX+Lua",
            "description": "The combination of NGINX+Lua is a huge swiss army knife for APIs and UIs alike. With NGINX+Lua, you can do many things including, but not limited to:\r\n- Authenticating Proxy\r\n- Rate Limiting (global & per client)\r\n-Dynamic Routing (for A/B testing)\r\n- Route Transformations (perhaps for migrating an existing API to use a new back end)\r\n- Data Transformations (convert JSON to XML, or XML to JSON, or any data format really)",
            "role": backend_dev_role
        },
        "One-Command-DevEnv": {
            "name": "One-Command-DevEnv",
            "description": "Create some automation around auto-magically provisioning a developer's environment so that it matches Production - with just one command.",
            "role": reliability_dev_role
        },
        "Packer-Images": {
            "name": "Packer-Images",
            "description": "Automate the creation of AMIs using Packer.",
            "role": reliability_dev_role
        },
        "Terraform": {
            "name": "Terraform",
            "description": "Identify if Terraform or a similar tool can help create immutable infrastructure.",
            "role": reliability_dev_role
        },
        "Varnish-API": {
            "name": "Varnish-API",
            "description": "APIs can benefit from caching too! Varnish is a quick win.",
            "role": backend_dev_role
        },
        "Varnish-UI": {
            "name": "Varnish-UI",
            "description": "Consider placing Varnish in front of the UI to reduce infrastructure costs while decreasing load time. Cache all the things!",
            "role": backend_dev_role
        },
        "PHP": {
            "name": "PHP",
            "description": "It's been many moons since I've worked with PHP, I'll probably need a refresher.",
            "role": learner_role
        },
        "Yoga": {
            "name": "Yoga",
            "description": "I practice 10-20 minutes of yoga at the beginning of every day. It gets me energized better than coffee.",
            "role": adventurer_role
        },
        "Bread-Winner": {
            "name": "Bread-Winner",
            "description": "I am the sole source of income for our family, and that's be choice! My wife is an amazing mother, and no one could take care of our kids better than her! I would love to be at home to help more than I am currently - and be there for impromptu adventures.",
            "role": asst_dir_role
        },
        "Maintenance": {
            "name": "Maintenance",
            "description": "I'm in charge of making sure the house doesn't fall down. I enjoy this responsibility, as things such as mowing the lawn is a source of exercise as well some quiet time to reflect.",
            "role": asst_dir_role
        },
        "Cycling-Instructor": {
            "name": "Cycling-Instructor",
            "description": "My daughter got a balance bike for her birthday, so we've been spending a lot of time learning how to ride it. She also has a tricycle for learning how to pedal.",
            "role": asst_dir_role
        },
        "Weekly-Ride": {
            "name": "Weekly-Ride",
            "description": "Every week during the summer several friends and I try to get together for a weekly mountain bike ride. I send out the reminders about when and where we are riding. I've been thinking about making a simple web app to do this, as well as randomly picking _where_ we ride for any given week.",
            "role": adventurer_role
        },
        "Bug-Fixes": {
            "name": "Bug-Fixes",
            "description": "There's nothing better than squashing bugs for users! Especially if you introduced it in the first place :)",
            "role": happiness_role
        },
        "Customer-Support": {
            "name": "Customer-Support",
            "description": "I see Customer Support as more than just reactively fixing problems. I really like to talk to users to find out what is great, and what could be better - and then act on it.",
            "role": happiness_role
        },
        "User": {
            "name": "User",
            "description": "I'm a Buffer user already. I like the product, but there are things I'd like to add. Such as tags - people love to organize things in their own ways. Or adding another 'Suggestions' track.",
            "role": happiness_role
        },
        "Web-Dev-Nanodegreee": {
            "name": "Web-Dev-Nanodegreee",
            "description": "I've started some classes in the Udacity Web Dev Nano Degree, but have yet to finish. I would really like to focus on that.",
            "role": learner_role
        },
        "Coursera": {
            "name": "Coursera",
            "description": "I recently took an 'Emotional Intelligence' class on Coursera. I really enjoyed it and would like to investigate other offerings. What really stuck with me from that course was that your brain can only be in the 'logic' or 'emotional' state at any one time - never both. That's really changed how I listen to others.",
            "role": learner_role
        },
    }

    for task in my_tasks:
        add_task(apps, my_tasks[task])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_add_roles'),
    ]

    operations = [
        migrations.RunPython(add_tasks),
    ]
