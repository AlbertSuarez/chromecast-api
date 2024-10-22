class Device:
    """
    ORM representing a Chromecast device
    """

    def __init__(self, chromecast_object):
        self.chromecast_object = chromecast_object
        self.uuid = str(self.chromecast_object.uuid)
        self.cast_type = self.chromecast_object.cast_type
        self.host = self.chromecast_object.host
        self.model_name = self.chromecast_object.model_name
        self.name = self.chromecast_object.name
        self.media_controller = self.chromecast_object.media_controller

    def has_device_name(self, device_name):
        """
        Check if the device has a given device name.
        :param device_name: Device name to check.
        :return: True if has the same device name, False otherwise.
        """
        return bool(self.name.lower().strip() == device_name.lower().strip())

    def serialize(self):
        """
        Serialize a ORM object to a Python dictionary.
        :return: Python dictionary representation of the Chromecast device.
        """
        return dict(
            uuid=self.uuid,
            cast_type=self.cast_type,
            host=self.host,
            model_name=self.model_name,
            name=self.name,
            media=dict(
                app_id=self.media_controller.app_id,
                is_active=self.media_controller.is_active,
                is_idle=self.media_controller.is_idle,
                is_paused=self.media_controller.is_paused,
                is_playing=self.media_controller.is_playing,
                title=self.media_controller.title,
                status=dict(
                    current_time=self.media_controller.status.current_time,
                    content_id=self.media_controller.status.content_id,
                    content_type=self.media_controller.status.content_type,
                    duration=self.media_controller.status.duration,
                    volume_level=self.media_controller.status.volume_level,
                    volume_muted=self.media_controller.status.volume_muted
                )
            )
        )
