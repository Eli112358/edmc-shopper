from logging import Logger, getLogger

# noinspection unresolved-references
from config import appname
from semantic_version import Version

from .preferences import Preferences
from .ui import UI

JsonData = dict[str, object]


class Shopper:
    plugin_dir: str

    def __init__(self, plugin_name: str, version: Version):
        self.plugin_name: str = plugin_name
        self.version: Version = version
        self.logger: Logger = getLogger(f"{appname}.{self.plugin_name}")
        self.preferences = Preferences(self)
        self.ui: UI = UI(self)

    def start(self, plugin_dir: str):
        self.plugin_dir = plugin_dir
        self.logger.debug(f"Starting plugin {self.plugin_name} from {plugin_dir}")
        return self.plugin_name.title()

    def stop(self):
        self.logger.debug(f"Stopping plugin {self.plugin_name}")

    def journal_entry(self, cmdr: str, is_beta: bool, system: str, station: str, entry: JsonData, state: JsonData):
        pass

    def capi_fleet_carrier(self, data: JsonData):
        pass
