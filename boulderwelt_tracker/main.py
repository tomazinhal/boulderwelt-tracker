import json
import logging
import requests
from time import sleep
from datetime import datetime
from dataclasses import dataclass


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


SLEEP = 60 * 15  # 15 Minutes
START_TIME = 7  # 7 AM
END_TIME = 23  # 11 PM

with open("config.json") as f:
    config = json.loads(f.read())

BOULDERWELTS = {"OST": config["OST"], "SUD": config["SUD"], "WEST": config["WEST"]}
PAYLOAD = config["PAYLOAD"]
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


@dataclass
class CrowdIndicator:
    """
    Serializer and Deserializer for the response from BW
    Example:
    """

    def __init__(self):
        pass


def save_response(data):
    """
    Saves data
    raises:
        ValueError
    """
    pass


def main():
    LOGGER.debug(datetime.now())
    for welt, url in BOULDERWELTS.items():
        response = requests.request("POST", url=url, data=PAYLOAD, headers=HEADERS)
        LOGGER.info(f"welt: {welt} - {response.text}")
    timeout_counter = 0
    while False:
        if START_TIME <= now() >= END_TIME:
            LOGGER.debug("Skipping query...")
        try:
            for welt, url in BOULDERWELTS.items():
                try:
                    response = requests.request(
                        "POST", url=url, data=PAYLOAD, headers=HEADERS
                    )
                    save_data(response.json())
                except TimeoutError:
                    LOGGER.exception(f"Boulderwelt {welt} time out")
            time.sleep(SLEEP)
        except ValueError as ve:
            LOGGER.exception(e)


if __name__ == "__main__":
    main()
