from logging import Logger, getLogger
from tkinter import Frame, StringVar

# noinspection unresolved-references,pep8-naming
import myNotebook as nb
# noinspection unresolved-references
from config import appname, config
from functools import partial
from semantic_version import Version
from tkinter.font import Font, nametofont

from ui import UI

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"


class Preferences:
    frame: nb.Frame
    mode_vars: dict[str, StringVar]
    rc_api_key_var: StringVar

    def __init__(self, shopper: Shopper):
        self.shopper = shopper

    def get_frame(self, parent: Frame) -> nb.Frame:
        self.frame = nb.Frame(parent)
        self.frame.columnconfigure(0, weight=0)
        section_font: Font = nametofont("TkDefaultFont").copy()
        section_font.configure(weight="bold")
        row: int = 0
        nb.Label(self.frame, text="Modes", font=section_font).grid(row=row, column=0)
        row += 1
        self.mode_vars: dict[str, StringVar] = {}
        self.mode_vars["general_trade"] = StringVar()
        self.mode_vars["general_trade"].set(config.get_str("edmc_shopper_mode_general_trade"))
        nb.Checkbutton(self.frame, text="General Trade", variable=self.mode_vars["general_trade"], onvalue="Yes", offvalue="No").grid(row=row, column=0)
        row += 1
        nb.Label(self.frame, text="Colonization", font=section_font).grid(row=row, column=0)
        row += 1
        nb.Label(self.frame, text="Raven Colonial API Key").grid(row=row, column=0)
        self.rc_api_key_var: StringVar = StringVar()
        self.rc_api_key_var.set(config.get_str("edmc_shopper_raven_colonial_api_key"))
        rc_api_key: nb.EntryMenu = nb.EntryMenu(self.frame, textvariable=self.rc_api_key_var, show="*")
        rc_api_key.grid(row=row, column=1)
        rc_api_key_toggle = partial(self._toggle_api_key_visibility, rc_api_key)
        nb.Button(self.frame, text="👁", width=3, command=rc_api_key_toggle).grid(row=row, column=2)
        return self.frame

    def _toggle_api_key_visibility(self, entry: nb.EntryMenu):
        chars = ["", "*"]
        entry.config(show=chars[1 - chars.index(entry.cget("show"))])

    def save(self):
        modes: dict[str, str] = {key: var.get() for key, var in self.mode_vars.items()}
        for mode, value in modes.items():
            config.set_str(f"edmc_shopper_mode_{mode}", value)
        rc_api_key: str = self.rc_api_key_var.get()
        config.set_str("edmc_shopper_raven_colonial_api_key", rc_api_key)
        self.shopper.logger.debug("Preferences saved")


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
