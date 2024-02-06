import json

from django.db import models

from .app import Application


class PayloadMapping(models.Model):
    """
    stores upstream applications payload mapping, maps from an
    application to server side payload keys\n
    app -> upstream application\n
    name -> identifier for the payload\n
    description -> a brief about the payload\n
    mappngJSON -> dumped json from upstream to server payload mapping
    """

    app = models.ForeignKey(Application,
                            on_delete=models.CASCADE,
                            related_name='payloadMappings')
    name = models.CharField(max_length=256)
    description = models.TextField()
    mappingJSON = models.TextField()

    class Meta:
        app_label = 'Platform'
        db_table = 'payload_mappings'

    def __str__(self):
        return f"{self.name} [{self.app.name}]"

    def to_dict(self):
        return {
            'app': self.app.name,
            'name': self.name,
            'desc': self.description,
            'mappingJSON': json.loads(self.mappingJSON)
        }
