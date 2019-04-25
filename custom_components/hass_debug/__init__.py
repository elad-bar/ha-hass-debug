import logging
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from .const import *

_LOGGER = logging.getLogger(__name__)

SERVICE_IS_ACTIVE_SCHEMA = vol.Schema({
    vol.Required(ATTR_STATE): cv.boolean,
})


def setup(hass, config):
    def debug_mode(service):
        state = service.data.get(ATTR_STATE, False)

        _LOGGER.info(f'Debug Mode changed to active: {state}')

        hass.loop.set_debug(state)

    hass.services.register(DOMAIN, SERVICE_IS_ACTIVE, debug_mode, schema=SERVICE_IS_ACTIVE_SCHEMA)

    return True
