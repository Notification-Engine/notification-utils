from django.db import models

from .app import Application


class Device(models.Model):
    device_id = models.CharField(max_length=36)
    fcm = models.CharField(max_length=255)
    connected_apps = models.ManyToManyField(
        Application, related_name='connected_devices')

    class Meta:
        app_label = 'Platform'
        db_table = 'devices'

    def __str__(self):
        return self.device_id
