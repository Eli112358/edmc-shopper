from logging import Logger, getLogger
from tkinter import Frame

# noinspection unresolved-references,pep8-naming
import myNotebook as nb
# noinspection unresolved-references
from config import appname, config
from semantic_version import Version

from preferences import Preferences
from ui import UI

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"


class Shopper:
    plugin_dir: str

    def __init__(self, plugin_name: str, version: Version):
        self.plugin_name: str = plugin_name
        self.version: Version = version
        self.logger: Logger = getLogger(f"{appname}.{self.plugin_name}")
        self.preferences = Preferences(self)
        self.ui: UI = UI(self)

    def plugin_start(self, plugin_dir: str):
        self.plugin_dir = plugin_dir
        self.logger.debug(f"Starting plugin {self.plugin_name} from {plugin_dir}")

    def plugin_stop(self):
        self.logger.debug(f"Stopping plugin {self.plugin_name}")

    def journal_entry(self, cmdr, system, station, entry, state):
        pass

    def capi_fleet_carrier(self, data):
        pass


this = Shopper(PLUGIN_NAME, Version(PLUGIN_VERSION))


def plugin_start3(plugin_dir: str):
    this.plugin_start(plugin_dir)
    return this.plugin_name.title()


def plugin_stop():
    this.plugin_stop()


def plugin_app(parent: Frame):
    return this.ui.get_frame(parent)


def plugin_prefs(parent: Frame, cmdr: str, is_beta: bool):
    return this.preferences.get_frame(parent)


def prefs_changed(cmdr: str, is_beta: bool):
    this.preferences.save()


def journal_entry(cmdr: str, system, station, entry, state):
    this.journal_entry(cmdr, system, station, entry, state)


# noinspection SpellCheckingInspection
def capi_fleetcarrier(data):
    this.capi_fleet_carrier(data)
