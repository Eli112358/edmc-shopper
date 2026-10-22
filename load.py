from tkinter import Frame

# noinspection unresolved-references,pep8-naming
import myNotebook as nb
# noinspection unresolved-references
from config import appname, config
from semantic_version import Version

from shopper import Shopper

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"

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
