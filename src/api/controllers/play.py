import time

import pychromecast

from src import RETRIEVE_RETRY, MESSAGE_PLAY_SUCCESS, MESSAGE_UNEXPECTED_ERROR, RETRIEVE_RTD, \
    MESSAGE_PLAY_DEVICE_NOT_FOUND
from src.api.services import response
from src.helper import log
from src.model.device import Device


def get(name, source_url):
    """
    API endpoint for playing a source to a device given its name.
    :param name: Device name.
    :param source_url: Source URL.
    :return: Source playing at given device.
    """
    try:
        for attempt in range(1, RETRIEVE_RETRY + 1):
            chromecast_list = pychromecast.get_chromecasts()
            chromecast_list = [Device(chromecast_item) for chromecast_item in chromecast_list]
            chromecast_list = [device for device in chromecast_list if device.has_device_name(name)]
            if chromecast_list:
                return response.make(error=False, response=dict(message=MESSAGE_PLAY_SUCCESS))
            else:
                log.warn(f'No devices found at attempt {attempt}.')
                time.sleep(RETRIEVE_RTD)
        log.warn(f'No devices found.')
        return response.make(error=True, message=MESSAGE_PLAY_DEVICE_NOT_FOUND)
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message=MESSAGE_UNEXPECTED_ERROR)
