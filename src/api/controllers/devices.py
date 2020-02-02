import time
import pychromecast

from src import MESSAGE_UNEXPECTED_ERROR, RETRIEVE_RETRY, RETRIEVE_RTD
from src.api.services import response
from src.helper import log
from src.model.device import Device


def get(name=None):
    """
    API endpoint for returning a given device by its name, all if name is not specified.
    :return: All devices.
    """
    try:
        for attempt in range(1, RETRIEVE_RETRY + 1):
            chromecast_list = pychromecast.get_chromecasts()
            chromecast_list = [Device(chromecast_item) for chromecast_item in chromecast_list]
            if name is not None:
                chromecast_list = [device for device in chromecast_list if device.has_device_name(name)]
            chromecast_list = [device.serialize() for device in chromecast_list]
            if chromecast_list:
                return response.make(error=False, response=dict(chromecast_list=chromecast_list))
            else:
                log.warn(f'No devices found at attempt {attempt}.')
                time.sleep(RETRIEVE_RTD)
        log.warn(f'No devices found.')
        return response.make(error=False, response=dict(chromecast_list=[]))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message=MESSAGE_UNEXPECTED_ERROR)
