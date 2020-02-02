import time

import pychromecast

from src import RETRIEVE_RETRY, MESSAGE_PLAY_SUCCESS, MESSAGE_UNEXPECTED_ERROR, RETRIEVE_RTD, \
    MESSAGE_PLAY_DEVICE_NOT_FOUND, MIME_TYPES, MESSAGE_PLAY_MIME_DEVICE_NOT_SUPPORTED
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
        log.info('Extracting source names...')
        source_ending = '.{}'.format(source_url.split('.')[-1])
        source_name = source_url.split('/')[-1]
        log.info(f'Source ending: [{source_ending}]')
        log.info(f'Source name: [{source_name}]')
        if source_ending not in MIME_TYPES:
            log.warn(MESSAGE_PLAY_DEVICE_NOT_FOUND)
            return response.make(error=True, message=MESSAGE_PLAY_DEVICE_NOT_FOUND)
        for attempt in range(1, RETRIEVE_RETRY + 1):
            log.info(f'Attempt [{attempt}]...')
            chromecast_list = pychromecast.get_chromecasts()
            chromecast_list = [Device(chromecast_item) for chromecast_item in chromecast_list]
            chromecast_list = [device for device in chromecast_list if device.has_device_name(name)]
            if chromecast_list:
                chromecast_device = chromecast_list[0]
                log.info(f'Chromecast device: [{chromecast_device.uuid} - {chromecast_device.name}]')
                log.info('Waiting for being loaded...')
                chromecast_device.chromecast_object.wait()
                log.info('Loaded.')
                mime_type = MIME_TYPES[source_ending]
                log.info(f'MIME type: [{mime_type}]')
                log.info(f'Cast type: [{chromecast_device.cast_type}]')
                if (chromecast_device.cast_type == 'audio' and 'video' in mime_type) or \
                        (chromecast_device.cast_type == 'group' and 'video' in mime_type):
                    log.warn(MESSAGE_PLAY_MIME_DEVICE_NOT_SUPPORTED)
                    return response.make(error=True, message=MESSAGE_PLAY_MIME_DEVICE_NOT_SUPPORTED)
                log.info('Playing media...')
                chromecast_device.chromecast_object.media_controller.play_media(
                    url=source_url,
                    content_type=mime_type,
                    title=source_name
                )
                chromecast_device.chromecast_object.media_controller.block_until_active()
                log.info('Done!')
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
