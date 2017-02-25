from __future__ import unicode_literals
from tenant_schemas.models import TenantMixin
from django.db import models

class tenantUser(TenantMixin):
    email = models.CharField(max_length = 100)
    name = models.CharField(max_length =100)