import base64
import json


def get_jwt_payload(payload_string):
    return json.loads(base64.b64decode(payload_string + "=" * ((4 - len(payload_string) % 4) % 4)))
