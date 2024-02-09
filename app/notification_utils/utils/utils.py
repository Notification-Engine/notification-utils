from functools import reduce

from .constants import DOT_SEPARATOR


def is_nested_key(key: str):
    return key.__contains__(DOT_SEPARATOR)


def is_nested_key_in_dict(key_chain: str, mapping: dict):
    keys = key_chain.split(DOT_SEPARATOR)
    for key in keys:
        if not key in mapping:
            return False
        mapping = mapping.get(key)
    return True


def get_nested_key_in_dict(key_chain: str, mapping: dict, multi_mode=False):
    keys = key_chain.split(DOT_SEPARATOR)
    return get_nested_key_in_dict_from_key_list(keys, mapping, multi_mode)


def get_nested_key_in_dict_from_key_list(keys: list, mapping, multi_mode=False):
    if len(keys) == 1:
        if multi_mode is True:
            return {
                keys[0]: mapping.get(keys[0])
            }
        return mapping.get(keys[0])

    if not isinstance(mapping, dict):
        return None

    if multi_mode is True:
        return {keys[0]: get_nested_key_in_dict_from_key_list(keys[1:], mapping.get(keys[0]), multi_mode)}

    return get_nested_key_in_dict_from_key_list(keys[1:], mapping.get(keys[0]), multi_mode)


def merge_two_dicts(dict1: dict, dict2: dict):
    for key, value in dict1.items():
        if isinstance(value, dict):
            node = dict2.setdefault(key, {})
            merge_two_dicts(value, node)
        else:
            dict2[key] = value

    return dict2


def merge_dicts(list_of_dicts: list):
    return reduce(merge_two_dicts, list_of_dicts)
