#!/usr/bin/python3
"""0-validate_utf8 module."""


# type: Union[bytes, str, int, List[Union[bytes, str]]] -> bool
def validUTF8(data):
    """
    validUTF8: determines if a given data set represents a valid \
        UTF-8 encoding.

    Args:
        data: list of integers.
    """
    if isinstance(data, int):
        try:
            data.to_bytes((data.bit_length() + 7) // 8,
                          byteorder='big').decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False
    elif isinstance(data, list):
        for d in data:
            if not validUTF8(d):
                return False
            return True
    elif isinstance(data, str) or isinstance(data, bytes):
        try:
            data.encode('utf-8').decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

    else:
        return False
