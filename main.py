from typing import Any, Optional

import decky_plugin
from settings import SettingsManager


class Plugin:
    def __init__(self) -> None:
        self.settings: Optional[SettingsManager] = None

    async def _main(self) -> None:
        self.settings = SettingsManager(
            name="config", settings_directory=decky_plugin.DECKY_PLUGIN_SETTINGS_DIR
        )

    async def _unload(self) -> None:
        pass

    async def set_setting(self, key: str, value: Any) -> None:
        if not self.settings:
            return
        self.settings.setSetting(key, value)

    async def get_setting(self, key: str, default: Any = None) -> Any:
        if not self.settings:
            return default
        return self.settings.getSetting(key, default)