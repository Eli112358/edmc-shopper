from logging import Logger
from tkinter import Frame, Label

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shopper import Shopper


class UI:
    frame: Frame

    def __init__(self, shopper: Shopper):
        self.shopper = shopper
        self.logger: Logger = shopper.logger.getChild("UI")

    def get_frame(self, parent: Frame) -> Frame:
        self.frame = Frame(parent)
        self.frame.grid_configure()
        message_text: str = f"Shopper v{self.shopper.version} loaded"
        message = Label(self.frame, text=message_text)
        message.grid()
        return self.frame
