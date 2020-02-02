RETRIEVE_RETRY = 5
RETRIEVE_RTD = 1.5

MIME_TYPES = {
    '.flv': 'video/x-flv',
    '.mp4': 'video/mp4',
    '.m3u8': 'application/x-mpegURL',
    '.ts': 'video/MP2T',
    '.3gp':	'video/3gpp',
    '.mov':	'video/quicktime',
    '.avi':	'video/x-msvideo',
    '.wmv':	'video/x-ms-wmv',
    '.mp3': 'audio/mpeg',
    '.ogg': 'audio/ogg',
    '.wave': 'audio/wav'
}

MESSAGE_UNEXPECTED_ERROR = 'Unexpected error.'
MESSAGE_PLAY_SUCCESS = 'Playing successfully.'
MESSAGE_PLAY_DEVICE_NOT_FOUND = 'Device not found with the given name.'
MESSAGE_PLAY_MIME_NOT_SUPPORTED = f'Source URL has to end in one of the following endings: {list(MIME_TYPES.keys())}'
MESSAGE_PLAY_MIME_DEVICE_NOT_SUPPORTED = 'The given source is not compatible with the given device.'
