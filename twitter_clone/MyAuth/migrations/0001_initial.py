# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(message='Usernames can contain only letters (A-Z),                                 digits and the underscore (_).', code='invalid_username', regex='^[A-Za-z0-9_]+$')], max_length=15, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=254, verbose_name='full name')),
                ('short_name', models.CharField(blank=True, max_length=30, verbose_name='short name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
