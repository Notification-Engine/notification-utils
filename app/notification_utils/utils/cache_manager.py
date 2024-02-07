import itertools
import json

from ..onboarding.models import PayloadMapping

PAYLOAD_MAPPING_PICKUP_CONDITIONS = {}


def refresh_payload_mapping_pickup_conditions():
    global PAYLOAD_MAPPING_PICKUP_CONDITIONS
    pickup_conditions = {}

    for payload in PayloadMapping.objects.all():
        payload_id = payload.id
        mapping_json = json.loads(payload.mappingJSON)
        payload_keys = get_payload_keys_from_mapping_json(mapping_json)
        pickup_conditions[payload_id] = payload_keys

    print("Successfully refreshed payload mapping cache")

    PAYLOAD_MAPPING_PICKUP_CONDITIONS = pickup_conditions

    return PAYLOAD_MAPPING_PICKUP_CONDITIONS


def get_payload_keys_from_mapping_json(mapping_json: dict):
    keys = mapping_json.values()
    return list(set(itertools.chain.from_iterable([k.split(',') for k in keys])))


def refresh_cache(cache_key=None):
    if cache_key is None or cache_key.lower() == 'all':
        refresh_payload_mapping_pickup_conditions()
        return

    refresh_payload_mapping_pickup_conditions()
