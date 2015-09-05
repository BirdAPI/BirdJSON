import json
from types import *
import re


class JsonObject(object):
    pass


def load_file(filename):
    with open(filename) as f:
        return load(f)


def load(fp):
    return _load(json.load(fp))


def loads(s):
    return _load(json.loads(s))


def _load(js):
    g = JsonObject()
    try:
        for key in js:
            _inject_value(g, key, js[key])
    except:
        return None
    return g


def _append_value(parent, value):
    if type(value) is ListType:
        l = []
        for v in value:
            _append_value(l, v)
        parent.append(l)
    elif type(value) is DictType:
        d = JsonObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.append(d)
    else:
        parent.append(value)


def _inject_value(parent, key, value):
    if type(value) is ListType:
        l = []
        for v in value:
            _append_value(l, v)
        parent.__dict__[_sanitize_key(key)] = l
    elif type(value) is DictType:
        d = JsonObject()
        for k, v in value.items():
            _inject_value(d, k, v)
        parent.__dict__[_sanitize_key(key)] = d
    else:
        parent.__dict__[_sanitize_key(key)] = value


def _sanitize_key(key):
    if re.match("^([0-9])", key):
        return "_" + key
    return key
