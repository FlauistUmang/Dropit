from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from time import time


def get_dest(instance,filename):
    return "%s_%s" % (str(time()).replace('.','_'), filename) 

class File(models.Model):
    file = models.FileField(upload_to =get_dest)