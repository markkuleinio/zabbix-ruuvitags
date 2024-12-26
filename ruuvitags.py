import logging
import logging.handlers

from ruuvitag_sensor.ruuvi import RuuviTagSensor


logger = logging.getLogger()


def handle_data(data):
    mac = data[0]
    temperature = data[1]["temperature"]
    humidity = data[1]["humidity"]
    rssi = data[1]["rssi"]
    logger.info(f"{mac} {temperature} {humidity} {rssi}")


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logging.getLogger("ruuvitag_sensor").setLevel(logging.ERROR)
    handler = logging.handlers.RotatingFileHandler(
        "/run/zabbix/ruuvitags.log",
        maxBytes=20000,
        backupCount=1,
    )
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    RuuviTagSensor.get_data(handle_data)
