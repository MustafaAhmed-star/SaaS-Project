
# Create your models here.
from django.db import models
from django. contrib.auth.models import Group, Permission

# Create your models here.
class Subscription(models.Model):
    name = models. CharField(max_length=120)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(Permission)
 
    class Meta:
        permissions = [
 ("basic", "Basic p"),
("pro", "Pro Perm"), # subscriptions.pro ("basic", "Basic Perm"), # subscriptions.b ("basic_ai", "Basic AI Perm")
("advanced", "Advanced Perm"), # subscriptions.
]