from django.db import models


class Event(models.Model):
    event_id = models.CharField(max_length=64)
    event_ts = models.DateField()
    title = models.TextField()
    description = models.TextField()
    metadata = models.TextField()

    class Meta:
        app_label = 'Processor'
        db_table = 'events'

    def __str__(self):
        return f"{self.event_id} ({self.title})"
