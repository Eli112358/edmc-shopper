from logging import Logger
from tkinter import StringVar, Frame

from functools import partial
# noinspection unresolved-references
from myNotebook import (
    Button as nbButton,
    Checkbutton as nbCheckbutton,
    EntryMenu as nbEntryMenu,
    Frame as nbFrame,
    Label as nbLabel,
)
from tkinter.font import Font, nametofont
from typing import TYPE_CHECKING

from .config import Config

if TYPE_CHECKING:
    from .shopper import Shopper


class Preferences:
    frame: nbFrame
    mode_vars: dict[str, StringVar]
    rc_api_key_var: StringVar

    def __init__(self, shopper: Shopper):
        self.shopper = shopper
        self.logger: Logger = shopper.logger.getChild("preferences")

    # noinspection unused-parameter
    def get_frame(self, parent: Frame, cmdr: str, is_beta: bool) -> nbFrame:
        self.frame = nbFrame(parent)
        self.frame.columnconfigure(0, weight=0)
        section_font: Font = nametofont("TkDefaultFont").copy()
        section_font.configure(weight="bold")
        row: int = 0
        nbLabel(self.frame, text="Modes", font=section_font).grid(row=row, column=0)
        row += 1
        nbLabel(self.frame, text="General Trade", font=section_font).grid(row=row, column=0)
        row += 1
        nbCheckbutton(
            self.frame,
            text=str(Config.GENERAL_TRADE.ENABLED),
            variable=Config.GENERAL_TRADE.ENABLED.tk_var(),
            onvalue=True,
            offvalue=False
        ).grid(row=row, column=0)
        row += 1
        nbLabel(self.frame, text="Colonization", font=section_font).grid(row=row, column=0)
        row += 1
        nbLabel(self.frame, text="Raven Colonial API Key").grid(row=row, column=0)
        rc_api_key: nbEntryMenu = nbEntryMenu(self.frame, textvariable=Config.RAVEN_COLONIAL.API_KEY.tk_var(), show="*")
        rc_api_key.grid(row=row, column=1)
        rc_api_key_toggle = partial(self._toggle_api_key_visibility, rc_api_key)
        nbButton(self.frame, text="👁", width=3, command=rc_api_key_toggle).grid(row=row, column=2)
        return self.frame

    @staticmethod
    def _toggle_api_key_visibility(entry: nbEntryMenu):
        chars = ["", "*"]
        entry.config(show=chars[1 - chars.index(entry.cget("show"))])

    # noinspection unused-parameter
    def save(self, cmdr: str, is_beta: bool):
        Config.save_all()
        self.logger.debug("Preferences saved")
