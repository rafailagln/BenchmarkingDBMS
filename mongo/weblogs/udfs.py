import re


def extract_ip(x):
    match = re.search(r"(^\S+) ", x)
    if match:
        return match[1]
    else:
        return ''


def extract_client_id(x):
    match = re.search(r"^\S+ (\S+) ", x)
    if match:
        return match[1]
    else:
        return ''


def extract_user_id(x):
    match = re.search(r"^\S+ \S+ (\S+) ", x)
    if match:
        return match[1]
    else:
        return ''


def extract_method(x):
    match = re.search(r'^.*"(\S+) \S+\s*\S*\s*"', x)
    if match:
        return match[1]
    else:
        return ''


def extract_endpoint(x):
    match = re.search(r'^.*"\S+ (\S+)\s*\S*\s*"', x)
    if match:
        return match[1]
    else:
        return ''


def extract_protocol(x):
    match = re.search(r'^.*"\S+ \S+\s*(\S*)\s*"', x)
    if match:
        return match[1]
    else:
        return ''


def extract_response_code(x):
    match = re.search(r'^.*" (\d{3}) ', x)
    if match:
        return int(match[1])
    else:
        return -1


def extract_content_size(x):
    match = re.search(r'^.*" \d{3} (\S+)', x)
    if match:
        return 0 if match[1] == '-' else int(match[1])
    else:
        return -1
