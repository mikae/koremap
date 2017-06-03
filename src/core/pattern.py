pattern_part_to_str_table = {}
str_to_pattern_part_table = {}

# from linux source
MAX_KEY_CODE = 0x2ff
# prevent dublers
MAX_KEY_CODE = MAX_KEY_CODE + 1


def _make_pattern(device_index, key_code):
    return MAX_KEY_CODE * device_index + key_code


def get_pattern(device_index, key_code):
    if device_index in pattern_part_to_str_table:
        device_pattern_parts = pattern_part_to_str_table[device_index]
        pass
    else:
        device_pattern_parts = {}
        pattern_part_to_str_table[device_index] = device_pattern_parts
        pass

    if key_code in device_pattern_parts:
        p = device_pattern_parts[key_code]
        pass
    else:
        p = _make_pattern(device_index, key_code)
        device_pattern_parts[key_code] = p
        pass

    return p


def pattern_to_arr(pattern, human=False):
    device_index = pattern / MAX_KEY_CODE
    key_code = pattern % MAX_KEY_CODE

    return [device_index, key_code]


def att_of_pattern_to_arr_of_arr(arr_of_pattern, human=False):
    assert isinstance(arr_of_pattern, list)

    res = []
    for pattern in arr_of_pattern:
        res.append(pattern_to_arr(pattern))
        pass

    return res
