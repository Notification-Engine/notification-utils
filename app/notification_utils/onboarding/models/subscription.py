from django.db import models

from .app import Application
from .device import Device
from .payload import PayloadMapping


class AppDeviceSubscriptions(models.Model):
    app = models.ForeignKey(
        Application, on_delete=models.CASCADE, related_name='device_subscriptions')
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name='app_subscriptions')
    payload = models.ForeignKey(
        PayloadMapping, on_delete=models.CASCADE, related_name='app_device_subscriptions')
    is_subscribed = models.BooleanField()

    class Meta:
        app_label = 'Platform'
        db_table = 'app_device_subscriptions'

    def __str__(self):
        return f"{self.app} - {self.device} | {self.payload} [{'Subscribed' if self.is_subscribed else 'Unsubscribed'}]"

    def get_frontend_data(self):
        payload_json = self.payload.to_dict()
        payload_json.update({
            'id': self.id,
            'is_subscribed': self.is_subscribed,
        })
        return payload_json
