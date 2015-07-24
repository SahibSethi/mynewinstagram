# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('code', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('country', models.ForeignKey(to='account.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='account.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(to='account.City', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
    ]
