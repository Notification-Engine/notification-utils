from django.db import models

from .app import Application


class AppInstance(models.Model):
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
        db_table = 'app_instances'
        constraints = [
            models.UniqueConstraint(fields=['device_id', 'connected_app'],
                                    name='unique app device combination')
        ]

    def __str__(self):
        return f"{self.connected_app} - {self.device_id}"
