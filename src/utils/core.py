import json
import os
from typing import Any


def json_encode(obj, pretty=False):
    try:
        return json.dumps(obj, ensure_ascii=False, indent=4 if pretty else None)
    except Exception as _:
        return None


def json_decode(text):
    try:
        return json.loads(text)
    except Exception:
        return None


def exists(path: str):
    return os.path.exists(path)


def make_dir(_dir: str):
    os.makedirs(os.path.dirname(_dir), exist_ok=True)


def read_string(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def write_string(path: str, text: str, append=False):
    path = os.path.abspath(path)
    if not exists(path):
        make_dir(path)
    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write(text)


def read_json(path: str):
    return json_decode(read_string(path))


def write_json(path: str, data: Any):
    write_string(path, json_encode(data, pretty=True) or "")
