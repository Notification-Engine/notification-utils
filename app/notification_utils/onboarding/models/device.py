from django.db import models

from .app import Application


class Device(models.Model):
    """
    Specifies an app instance on a device
    [DOES NOT UNIQUELY IDENTIFY A DEVICE]
    """
    device_id = models.CharField(max_length=36)
    fcm = models.CharField(max_length=255)
    connected_app = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='connected_devices',
        null=True)

    class Meta:
        app_label = 'Platform'
        db_table = 'devices'

    def __str__(self):
        return self.device_id
