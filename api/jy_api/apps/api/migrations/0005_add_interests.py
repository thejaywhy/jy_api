# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_interest(apps, interest={}):
    """
    Create a new instance of the Interest object
    """
    Interest = apps.get_model("api", "Interest")

    new_interest = Interest.objects.create(
        name=interest["name"],
        description=interest["description"],
        role=interest["role"]
    )
    new_interest.save()


def add_interests(apps, schema_editor):
    """
    Initial Dataset for the "Interest" resource.
    """

    Role = apps.get_model("api", "Role")

    adventurer_role = Role.objects.get(name="Adventurer")
    asst_dir_role = Role.objects.get(name="Assistant-Director-of-Childhood-Experience")
    backend_dev_role = Role.objects.get(name="Backend-Developer")
    happiness_role = Role.objects.get(name="Happiness-Hero")
    learner_role = Role.objects.get(name="Lifelong-Learner")
    reliability_dev_role = Role.objects.get(name="Reliability-Developer")


    my_interests = {
        "Ansible": {
            "name": "Ansible",
            "description": "My experience with Ansible is limited. I first looked at it several years ago, before it matured. I've since checked it out and played with it a little bit, but not much. I'd like to work with it more. ",
            "role": reliability_dev_role
        },
        "Automated-Acceptance-Testing": {
            "name": "Automated-Acceptance-Testing",
            "description": "When used in conjunction with a Continuous Deployment pipeline, Automated Acceptance Testing give good feedback when a feature is ready to be deployed or broken. Having automated tests sure does beat doing manual testing - but AAT is not a replacement for all forms of manual tests.",
            "role": reliability_dev_role
        },
        "My-Wife": {
            "name": "My-Wife",
            "description": "My wife is my best friend, and I rely on her completely. I've never not wanted to spend more time with her. She challenges me to be a better version of myself everyday.",
            "role": asst_dir_role
        },
        "My-Daughter": {
            "name": "My-Daughter",
            "description": "At just two-and-half years old, Reagan already has me under her control :) She's a cutie, and super smart, learning new things every day. Our favorite things to do together are play outside and build with Legos. The best part is she looks like my mini-me.",
            "role": asst_dir_role
        },
        "My-Son": {
            "name": "My-Son",
            "description": "At just a month old, our relationship is pretty simple. But I can't wait to see him grow up and turn into another mini-me.",
            "role": asst_dir_role
        },
        "baking": {
            "name": "baking",
            "description": "Teaching my 2.5 year old daughter how to bake! And my son when he gets old enough.",
            "role": asst_dir_role
        },
        "Bash": {
            "name": "Bash",
            "description": "I like to use Bash for wrapper scripts to other functionality, especially for automating common operations on developer's machines. However, I do _not_ think bash is a good tool for automating production deployments.",
            "role": reliability_dev_role
        },
        "TDD": {
            "name": "TDD",
            "description": "Test Driven Development is a great way to instil confidence in your code, and lets you know when you are have created the minimal feature.",
            "role": backend_dev_role
        },
        "BDD": {
            "name": "BDD",
            "description": "Behavior Driven Development is a pretty neat way to write tests. I especially like the format of:\r\nGiven...\r\nWhen...\r\nThen...\r\n\r\nIt make for an easy to follow test pattern. ",
            "role": backend_dev_role
        },
        "C": {
            "name": "C",
            "description": "I've spent the majority of my career writing high performance C for embedded applications. I've been using it less and less, but it is a handy tool to have, especially when working with Varnish or NGINX modules. ",
            "role": backend_dev_role
        },
        "Chef": {
            "name": "Chef",
            "description": "I've worked on numerous production cookbooks for deploying Varnish, NGINX, and Django Apps. I felt chef had a steeper learning curve than some of the other tools, but it does solve a lot of the harder problems associated with deploying services at scale. ",
            "role": reliability_dev_role
        },
        "Continuous-Deployment": {
            "name": "Continuous-Deployment",
            "description": "A continuous deployment pipeline allows for reliability deploying something known to work. It should also allow for seamless rollback. I'd like to learn what is already being used, and expand upon it. ",
            "role": reliability_dev_role
        },
        "Continuous-Integration": {
            "name": "Continuous-Integration",
            "description": "Continuous Integration aids developers by given them continuous feedback on the state of a project. This has immense value when coupled with unit tests. I'd like to learn what is already in use, and then expand upon it. ",
            "role": reliability_dev_role
        },
        "Go": {
            "name": "Go",
            "description": "I'm a big fan of go, but have only been able to use it for side projects so far. The syntax is easy for me to learn because it's similar to C. But it has so much support in it's stdlib! An increasing number of open source tools are being built in go, it's nice to know how to dig into them and figure out how they work. ",
            "role": backend_dev_role
        },
        "Reading": {
            "name": "Reading",
            "description": "In love reading for myself, but also for my kids. We read several books together ever day. I also read for about an hour a day. My interests recently have included Reinventing Organizations, Delivering Happiness, and I am Fat (so a big mix). My all time favorite book is 'A Prayer for Owen Meany'",
            "role": learner_role
        },
        "Crosswords": {
            "name": "Crosswords",
            "description": "My wife and I try to do a crossword together at least once a week (less recently, newborns like to mess with your schedule). Crosswords are a great way to challenge the mind, while also learning some (mostly useless) facts.",
            "role": learner_role
        },
        "Software-Languages": {
            "name": "Software-Languages",
            "description": "I enjoy learning new software languages because they challenge me to think about problems in different ways. I'd like to take a look at Elixir/Erlang next. My only previous experience with Erlang is the load testing tool Tsung, but I liked what I saw.",
            "role": learner_role
        },
        "Agile-Methodologies": {
            "name": "Agile-Methodologies",
            "description": "I've been a Scrum Master for the past year, and it's challenged the way I think about how I plan; not just software, but in life. There are of course many Agile methods, and it's interesting to apply them on a personal level. I disagree with the blank enforcement of Agile as a process - instead use it as a guideline.",
            "role": learner_role
        },
        "Mountain-Biking": {
            "name": "Mountain-Biking",
            "description": "My dad introduced me to cycling at a very young age, and it's always been an important part of my life. I'd rather ride my bike than drive a car. Even after a 'bad' ride, I have a feeling of peace.",
            "role": adventurer_role
        },
        "Hiking": {
            "name": "Hiking",
            "description": "Walking in the woods really gives you a chance to slow down and think about things. The feeling of accomplishment after a long (or short) hike just can't be beat. I can't wait to share this with my children.",
            "role": adventurer_role
        },
         "Skiing": {
            "name": "Skiing",
            "description": "I don't ski as much as I used to (it's expensive!), but it's long been how I quench my need for speed.",
            "role": adventurer_role
        },
        "Rock-Climbing": {
            "name": "Rock-Climbing",
            "description": "It requires immense focus to make it safely to the top of a wall, it really requires you to clear your mind.",
            "role": adventurer_role
        },
        "Ultimate-Frisbee": {
            "name": "Ultimate-Frisbee",
            "description": "Playing competitive ultimate taught me the importance of knowing your teammates on and off the field. Knowing motivations for others helps form a more productive team - and I think that applies to the work place too. I don't play as much Ultimate as I used to, but I still try to play pick up here and there - it's an amazing full body work out.",
            "role": adventurer_role
        },
         "Home-Brewing": {
            "name": "Home-Brewing",
            "description": "Home Brewing Beer is always an adventure - in both art and process. It's an art form to craft a good recipe, but it's a process to make it repeatable. Always learning from my mistakes to improve the next batch.",
            "role": learner_role
        },
    }

    for interest in my_interests:
        add_interest(apps, my_interests[interest])


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_add_tasks'),
    ]

    operations = [
        migrations.RunPython(add_interests),
    ]
