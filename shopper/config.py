from dataclasses import dataclass, fields
from pathlib import Path
from tkinter import Variable, BooleanVar, IntVar, StringVar

from enum import Enum

# noinspection unresolved-references
from config import appname as edmc_app_name, config as edmc_config

from load import PLUGIN_NAME

SupportedTypes = int | str | list[str] | bool
NOT_IMPLEMENTED_TEMPLATE: str = "Cannot handle get value of type {}"

ROOT = Path(PLUGIN_NAME)

class ConfigGroup(Enum):

    def __init__(self, path: Path, var_type: type, default: object=None):
        self._path = path
        self.key = str(path).replace("/", ".")
        self.var_type = var_type
        self.default = default

    def __str__(self):
        return self.name

    @classmethod
    def save_all(cls):
        for key in cls.__dict__.keys():
            cls.__dict__[key].save()

    def get(self) -> SupportedTypes:
        if self.var_type == bool:
            return self.get_bool()
        if self.var_type == int:
            return self.get_int()
        if self.var_type == str:
            return self.get_str()
        if self.var_type == list:
            return self.get_list()

        raise NotImplementedError(NOT_IMPLEMENTED_TEMPLATE.format(self.var_type))

    def get_bool(self) -> bool:
        return edmc_config.get_bool(self.key, default=self.default)

    def get_int(self) -> int:
        return edmc_config.get_int(self.key, default=self.default)

    def get_str(self) -> str:
        return edmc_config.get_str(self.key, default=self.default)

    def get_list(self) -> list:
        return edmc_config.get_list(self.key, default=self.default)

    def save(self):
        self.set(self.tk_var().get())

    def set(self, value: SupportedTypes):
        edmc_config.set(self.key, value)

    def tk_var(self) -> Variable:
        if self.var_type == bool:
            return BooleanVar(value=self.get_bool())
        if self.var_type == int:
            return IntVar(value=self.get_int())
        if self.var_type == str:
            return StringVar(value=self.get_str())

        # noinspection string-conversion-without-dunder-method
        raise NotImplementedError(NOT_IMPLEMENTED_TEMPLATE.format(self.var_type))

    def tk_str_var(self) -> StringVar:
        return StringVar(value=str(self.get()))


# noinspection unresolved-references
class GeneralTrade(ConfigGroup):
    _ROOT = ROOT / "general_trade", None, None
    ENABLED = _ROOT[0] / "enabled", bool, True


# noinspection unresolved-references
class RavenColonial(ConfigGroup):
    _ROOT = ROOT / "raven_colonial", None, None
    API_KEY = _ROOT[0] / "api_key", str, ""

# noinspection unresolved-references
class StarMap(ConfigGroup):
    _ROOT = ROOT / "star_map", None, None
    RADIUS = _ROOT[0] / "radius", int, 50

@dataclass
class Config:
    GENERAL_TRADE = GeneralTrade
    RAVEN_COLONIAL = RavenColonial
    STAR_MAP = StarMap

    @classmethod
    def app_name(cls):
        return edmc_app_name

    @classmethod
    def save_all(cls):
        field: ConfigGroup
        for field in fields(cls):
            field.save_all()
