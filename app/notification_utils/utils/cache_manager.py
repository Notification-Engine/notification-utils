import json

from ..onboarding.models import PayloadMapping

PAYLOAD_MAPPING_PICKUP_CONDITIONS = {}


def refresh_payload_mapping_pickup_conditions():
    global PAYLOAD_MAPPING_PICKUP_CONDITIONS
    pickup_conditions = {}

    for payload in PayloadMapping.objects.all():
        payload_id = payload.id
        mapping_json = json.loads(payload.mappingJSON)
        payload_keys = list(mapping_json.keys())
        pickup_conditions[payload_id] = payload_keys

    PAYLOAD_MAPPING_PICKUP_CONDITIONS = pickup_conditions

    return PAYLOAD_MAPPING_PICKUP_CONDITIONS


def refresh_cache(cache_key):
    refresh_payload_mapping_pickup_conditions()
