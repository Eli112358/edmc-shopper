from functools import partial
from tkinter import StringVar, Frame
from tkinter.font import Font, nametofont

from shopper import Shopper


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
