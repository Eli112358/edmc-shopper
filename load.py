# noinspection unresolved-references
from config import appname
from logging import Logger, getLogger
from tkinter import Frame, Label

from semantic_version import Version

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"


class UI:
    frame: Frame

    def __init__(self, shopper: Shopper):
        self.shopper = shopper

    def get_frame(self, parent: Frame) -> Frame:
        self.frame = Frame(parent)
        self.frame.grid_configure()
        message_text: str = f"Shopper v{self.shopper.version} loaded"
        message = Label(self.frame, text=message_text)
        message.grid()
        return self.frame


class Shopper:
    def __init__(self, plugin_name: str, version: Version):
        self.plugin_name: str = plugin_name
        self.version: Version = version
        self.ui: UI = UI(self)
        self.logger: Logger = getLogger(f"{appname}.{self.plugin_name}")

    def plugin_start(self, plugin_dir: str):
        self.logger.debug(f"Starting plugin {self.plugin_name} from {plugin_dir}")

    def plugin_stop(self):
        self.logger.debug(f"Stopping plugin {self.plugin_name}")


this = Shopper(PLUGIN_NAME, Version(PLUGIN_VERSION))


def plugin_start3(plugin_dir: str):
    this.plugin_start(plugin_dir)
    return this.plugin_name


def plugin_stop():
    this.plugin_stop()


def plugin_app(parent: Frame):
    return this.ui.get_frame(parent)
