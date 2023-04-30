import asyncio
from sensornetwork.sensor.ds18b20 import DS18B20
from sensornetwork import HOST_INFO


async def main(host: str, port: int):
    
    await asnycio.sleep(0.1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
