from django_kafka import kafka_listener

from .cache_manager import refresh_cache
from .constants import REFRESH_CACHE_KAFKA_KEY


@kafka_listener
def notification_global_listener(message, listener_method=None, *args, **kwargs):
    if message.key().decode('utf-8') == REFRESH_CACHE_KAFKA_KEY:
        return refresh_cache(message.value().decode('utf-8'))

    if listener_method is not None:
        return listener_method(message, *args, **kwargs)
