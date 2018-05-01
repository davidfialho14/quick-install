from abc import abstractmethod
from typing import NamedTuple

from quick_installer.app import Application


class Source(NamedTuple):
    repository: str
    name: str
    key_url: str


class AptPackage(Application):
    source: Source = None
    ppa: str = None

    @property
    @abstractmethod
    def package(self) -> str:
        pass

    def setup(self, full=False):

        if self.source:
            apt.add_source(*self.source)

        if self.ppa:
            apt.add_ppa(self.ppa)

        if full:
            apt.update()

    def install(self):
        apt.install(self.package)

    def cleanup(self):
        pass

    def is_installed(self):
        return apt.is_package_installed(self.package)