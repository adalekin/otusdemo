import requests
from talepy.steps import Step

from orders import settings

AFFO_SESSION = requests.Session()


def _affo_api(path):
    return settings.AFFO_URL + path


class SendEvent(Step):
    def execute(self, state):
        if "tid" not in state or "cid" not in state:
            return state

        response = AFFO_SESSION.post(
            _affo_api("/events/"),
            json={
                "t": "event",
                "tid": state["tid"],
                "cid": state["cid"],
                "cn": state["cn"],
                "cs": state["cs"],
                "ec": state["ec"],
                "ea": state.get("ea"),
                "el": state.get("el"),
                "ev": state.get("ev"),
            },
        )
        response.raise_for_status()

        return state

    def compensate(self, state):
        pass
