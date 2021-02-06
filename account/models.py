from django.db import models

from django.contrib.auth.models import Group

Group.add_to_class('access_flag', models.BooleanField(default=True))

