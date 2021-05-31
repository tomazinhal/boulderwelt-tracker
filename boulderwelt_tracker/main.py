import json
import logging
import requests
from time import sleep
from datetime import datetime


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
file_handler = logging.FileHandler("logfile.log")
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
file_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)

SLEEP = 60 * 15  # 15 Minutes
START_TIME = 7  # 7 AM
END_TIME = 23  # 11 PM

with open("config.json") as f:
    config = json.loads(f.read())

BOULDERWELTS = {"OST": config["OST"], "SUD": config["SUD"], "WEST": config["WEST"]}
PAYLOAD = config["PAYLOAD"]
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


def save_data(welt, data):
    """
    Saves data
    raises:
        ValueError
    """
    data["welt"] = welt
    data["timestamp"] = datetime.now().isoformat()
    with open(f"{welt}.json", "w+") as f:
        LOGGER.debug(f"Dumping {data} to file")
        json.dump(data, f)


def main(debug=False):
    if debug:
        LOGGER.debug(datetime.now())
        for welt, url in BOULDERWELTS.items():
            response = requests.request("POST", url=url, data=PAYLOAD, headers=HEADERS)
            LOGGER.info(f"welt: {welt} - {response.text}")
            save_data(welt, response.json())
        return
    while True:
        cur_hour = datetime.now().hour
        if (cur_hour < START_TIME) or (cur_hour > END_TIME):
            LOGGER.info("Skipping query...")
        try:
            for welt, url in BOULDERWELTS.items():
                try:
                    response = requests.request(
                        "POST", url=url, data=PAYLOAD, headers=HEADERS
                    )
                    save_data(welt, response.json())
                except TimeoutError:
                    LOGGER.exception(f"Boulderwelt {welt} time out")
            time.sleep(SLEEP)
        except ValueError as ve:
            LOGGER.exception(e)


if __name__ == "__main__":
    main()
