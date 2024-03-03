from django.db import models
from django.utils import timezone


class Application(models.Model):
    appId = models.CharField(max_length=36)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    subscriptions = models.ManyToManyField(
        'PayloadMapping', related_name='subscribed_apps')
    android_appname = models.CharField(max_length=30, null=True, blank=True)
    android_package = models.CharField(max_length=256, null=True, blank=True)
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
