from logging import Logger, getLogger
from pathlib import Path

from semantic_version import Version

from .config import Config
from .preferences import Preferences
from .ui import UI

JsonData = dict[str, object]


class Shopper:
    plugin_dir: Path

    def __init__(self, plugin_name: str, version: Version):
        self.plugin_name: str = plugin_name
        self.version: Version = version
        self.logger: Logger = getLogger(f"{Config.app_name()}.{self.plugin_name}")
        self.preferences = Preferences(self)
        self.ui: UI = UI(self)

    def start(self, plugin_dir: str):
        self.logger.debug(f"Starting plugin {self.plugin_name} from {plugin_dir}")
        self.plugin_dir = Path(plugin_dir)
        return self.plugin_name.title()

    def stop(self):
        self.logger.debug(f"Stopping plugin {self.plugin_name}")

    def journal_entry(self, cmdr: str, is_beta: bool, system: str, station: str, entry: JsonData, state: JsonData):
        pass

    def capi_fleet_carrier(self, data: JsonData):
        pass
