import importlib
from typing import Dict, Iterator

from quick_installer import settings
from quick_installer.application import Application


class Repository:
    source = 'quick_installer.applications'

    def __init__(self):
        # Stores a applications indexed by their names
        # For each application stores a set of attributes defined by 'AppAttributes'
        self.applications: Dict[str, Application] = {}

        # Load the module containing the applications
        apps_module = importlib.import_module(self.source)

        # Look for all application classes inside that module
        for name, cls in apps_module.__dict__.items():

            if isinstance(cls, type) and name.endswith("Application"):
                if name == "Application":
                    # Ignore the generic 'Application'
                    continue

                # Found an Application class
                application = cls()
                self.applications[application.name] = application

    def all(self) -> Iterator[Application]:
        return iter(app for app in self.applications.values())

    def system_apps(self) -> Iterator[Application]:
        return iter(app for app in self.applications.values() if type(app) in settings.SYSTEM_APPS)

    def find_by_name(self, name: str) -> Application:
        return self.applications[name]
