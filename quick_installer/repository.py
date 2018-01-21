import importlib
from typing import Dict, Iterator, NamedTuple

from quick_installer.application import Application
from quick_installer.enable import EnabledApplication


class App(NamedTuple):
    application: Application
    enabled: bool


class Repository:
    source = 'quick_installer.applications'

    def __init__(self):
        # Stores a applications indexed by their names
        # For each application stores a set of attributes defined by 'AppAttributes'
        self.applications: Dict[str, App] = {}

        # Load the module containing the applications
        apps_module = importlib.import_module(self.source)

        # Look for all application classes inside that module
        for name, cls in apps_module.__dict__.items():

            if isinstance(cls, type) and name.endswith("Application"):
                if name == "Application":
                    # Ignore the 'Application' interface
                    continue

                # Found an Application class that is disabled
                application = cls()
                self.applications[application.name] = App(application, enabled=False)

            if isinstance(cls, EnabledApplication):
                # Found an Application class that is enabled
                application = cls()
                self.applications[application.name] = App(application, enabled=True)

    def all(self) -> Iterator[Application]:
        return iter(app.application for app in self.applications.values())

    def enabled(self) -> Iterator[Application]:
        return iter(app.application for app in self.applications.values() if app.enabled)

    def find_by_name(self, name: str) -> Application:
        return self.applications[name].application
