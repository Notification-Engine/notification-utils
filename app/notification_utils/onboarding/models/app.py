from django.db import models
from django.utils import timezone


class Application(models.Model):
    appId = models.CharField(max_length=16)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'Platform'
        db_table = 'applications'

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "appId": self.appId,
            "name": self.name,
            "created_at": str(self.created_at)
        }
