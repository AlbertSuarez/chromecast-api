import pychromecast

from src import MESSAGE_UNEXPECTED_ERROR
from src.api.services import response
from src.helper import log
from src.model.device import Device


def get_all():
    """
    API endpoint for returning all devices within the local network.
    :return: All devices.
    """
    try:
        chromecast_list = pychromecast.get_chromecasts()
        chromecast_list = [Device(chromecast_item) for chromecast_item in chromecast_list]
        chromecast_list = [device.serialize() for device in chromecast_list]
        return response.make(error=False, response=dict(chromecast_list=chromecast_list))
    except Exception as e:
        log.error(f'Unexpected error: [{e}]')
        log.exception(e)
        return response.make(error=True, message=MESSAGE_UNEXPECTED_ERROR)
