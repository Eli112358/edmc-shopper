from tkinter import Frame

# noinspection unresolved-references
from myNotebook import Frame as nbFrame
from semantic_version import Version
from typing import Callable

from shopper.shopper import Shopper, JsonData

PLUGIN_NAME = "shopper"
PLUGIN_VERSION = "0.0.0"

this: Shopper = Shopper(PLUGIN_NAME, Version(PLUGIN_VERSION))

# noinspection SpellCheckingInspection
capi_fleetcarrier: Callable[[JsonData], None] = this.capi_fleet_carrier
journal_entry: Callable[[str, bool, str, str, JsonData, JsonData], None] = this.journal_entry
plugin_app: Callable[[Frame], Frame] = this.ui.get_frame
plugin_prefs: Callable[[Frame, str, bool], nbFrame] = this.preferences.get_frame
plugin_start3: Callable[[str], str] = this.start
plugin_stop: Callable[[], None] = this.stop
prefs_changed: Callable[[str, bool], None] = this.preferences.save
