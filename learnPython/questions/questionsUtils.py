def create_sub_string_chars_dict(sub_string: str) -> dict:
    ret_dict = {}
    for c in sub_string:
        if c in ret_dict:
            ret_dict[c] += 1
        else:
            ret_dict[c] = 1

    return ret_dict
