# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('account', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/', blank=True)),
                ('following', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
