from logging import Logger
from pathlib import Path
from tkinter import StringVar, Frame, BooleanVar

# noinspection unresolved-references
from config import config
from functools import partial
# noinspection unresolved-references
from myNotebook import (
    Button as nbButton,
    Checkbuton as nbCheckbutton,
    EntryMenu as nbEntryMenu,
    Frame as nbFrame,
    Label as nbLabel,
)
from tkinter.font import Font, nametofont
from typing import TYPE_CHECKING

CONFIG_NAME_SEPARATOR: str = "_"

if TYPE_CHECKING:
    from .shopper import Shopper

MODES: list[str] = [
    "general_trade",
]


class Preferences:
    frame: nbFrame
    mode_vars: dict[str, StringVar]
    rc_api_key_var: StringVar

    def __init__(self, shopper: Shopper):
        self.shopper = shopper
        self._config_base: Path = Path(self.shopper.plugin_name.lower())
        self.logger: Logger = shopper.logger.getChild("preferences")

    def get_name(self, keys: Path) -> str:
        return str(self._config_base / keys.relative_to(self._config_base)).replace("/", CONFIG_NAME_SEPARATOR)

    def get_frame(self, parent: Frame, cmdr: str, is_beta: bool) -> nbFrame:
        self.frame = nbFrame(parent)
        self.frame.columnconfigure(0, weight=0)
        section_font: Font = nametofont("TkDefaultFont").copy()
        section_font.configure(weight="bold")
        row: int = 0
        nbLabel(self.frame, text="Modes", font=section_font).grid(row=row, column=0)
        row += 1
        self.mode_vars: dict[str, BooleanVar] = {mode: BooleanVar() for mode in MODES}
        modes_path = self._config_base / "mode"
        for mode, variable in self.mode_vars.items():
            variable.set(config.get_bool(self.get_name(modes_path / mode)))
            text: str = mode.replace("_", " ").title()
            nbCheckbutton(self.frame, text=text, variable=variable, onvalue=True, offvalue=False).grid(row=row, column=0)
            row += 1
        nbLabel(self.frame, text="Colonization", font=section_font).grid(row=row, column=0)
        row += 1
        nbLabel(self.frame, text="Raven Colonial API Key").grid(row=row, column=0)
        self.rc_api_key_var: StringVar = StringVar()
        raven_colonial = self._config_base / "raven_colonial"
        self.rc_api_key_var.set(config.get_str(self.get_name(raven_colonial / "api_key")))
        rc_api_key: nbEntryMenu = nbEntryMenu(self.frame, textvariable=self.rc_api_key_var, show="*")
        rc_api_key.grid(row=row, column=1)
        rc_api_key_toggle = partial(self._toggle_api_key_visibility, rc_api_key)
        nbButton(self.frame, text="👁", width=3, command=rc_api_key_toggle).grid(row=row, column=2)
        return self.frame

    @staticmethod
    def _toggle_api_key_visibility(entry: nbEntryMenu):
        chars = ["", "*"]
        entry.config(show=chars[1 - chars.index(entry.cget("show"))])

    def save(self, cmdr: str, is_beta: bool):
        modes: dict[str, bool] = {key: variable.get() for key, variable in self.mode_vars.items()}
        modes_path = self._config_base / "mode"
        for mode, value in modes.items():
            config.set(self.get_name(modes_path / mode), value)
        raven_colonial = self._config_base / "raven_colonial"
        rc_api_key: str = self.rc_api_key_var.get()
        config.set(self.get_name(raven_colonial / "api_key"), rc_api_key)
        self.logger.debug("Preferences saved")
