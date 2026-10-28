import asyncio
import logging
import logging.handlers

from ruuvitag_sensor.ruuvi import RuuviTagSensor


logger = logging.getLogger()


async def main():
    async for found_data in RuuviTagSensor.get_data_async():
        mac, data = found_data
        temperature = data["temperature"]
        humidity = data["humidity"]
        rssi = data["rssi"]
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

    asyncio.run(main())
