from tkinter import Frame

# noinspection unresolved-references,pep8-naming
import myNotebook as nb
from semantic_version import Version
from typing import Callable

from shopper import Shopper, JsonData

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"

this: Shopper = Shopper(PLUGIN_NAME, Version(PLUGIN_VERSION))


def plugin_start3(plugin_dir: str):
    this.start(plugin_dir)
    return this.plugin_name.title()


def plugin_stop():
    this.stop()


def plugin_app(parent: Frame):
    return this.ui.get_frame(parent)


def plugin_prefs(parent: Frame, cmdr: str, is_beta: bool):
    return this.preferences.get_frame(parent, cmdr, is_beta)


def prefs_changed(cmdr: str, is_beta: bool):
    this.preferences.save(cmdr, is_beta)


def journal_entry(cmdr: str, is_beta: bool, system: str, station: str, entry: JsonData, state: JsonData):
    this.journal_entry(cmdr, is_beta, system, station, entry, state)


# noinspection SpellCheckingInspection
def capi_fleetcarrier(data: JsonData):
    this.capi_fleet_carrier(data)
