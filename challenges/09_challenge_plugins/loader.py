import importlib
from typing import List


class PluginInterface:
    def load(self) -> None:
        """Load the plugin into the application."""
        ...


def import_plugin(name: str) -> PluginInterface:
    return importlib.import_module(name) # type: ignore


def load_plugins(plugins: List[str]) -> None:
    for plugin_name in plugins:
        plugin = import_plugin(plugin_name)
        plugin.load()