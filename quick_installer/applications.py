from abc import abstractmethod
from typing import NamedTuple

from quick_installer.application import Application
from quick_installer.installers import apt, snap


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
        apt.is_package_installed(self.package)


class Snap(Application):
    snap = None
    options = None

    @property
    def name(self) -> str:
        return self.snap

    def setup(self, full=False):
        pass

    def install(self):
        snap.install(self.snap, self.options)

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return snap.is_snap_installed(self.snap)


class SignalApplication(AptPackage):
    name = "signal"
    package = 'signal-desktop'
    source = Source(
        repository="deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main",
        name="signal",
        key_url="https://updates.signal.org/desktop/apt/keys.asc"
    )


class ChromeApplication(AptPackage):
    name = "chrome"
    package = 'google-chrome-stable'
    source = Source(
        repository="deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main",
        name="google-chrome",
        key_url="https://dl-ssl.google.com/linux/linux_signing_key.pub"
    )


class SeafileApplication(AptPackage):
    name = "seafile"
    package = 'seafile-gui'
    ppa = 'ppa:seafile/seafile-client'


class EnpassApplication(AptPackage):
    name = "enpass"
    package = 'enpass'
    ppa = 'ppa:seafile/seafile-client'
    source = Source(
        repository="deb http://repo.sinew.in/ stable main",
        name="enpass",
        key_url="https://dl.sinew.in/keys/enpass-linux.key"
    )


class AtomApplication(Snap):
    snap = 'atom'
    options = ['classic']


class SlackApplication(Snap):
    snap = 'slack'
    options = ['classic']


class IntellijIDEAApplication(Snap):
    snap = 'intellij-idea-ultimate'
    options = ['classic']


class PyCharmApplication(Snap):
    snap = 'pycharm-professional'
    options = ['classic']


class SublimeApplication(Snap):
    snap = 'sublime-text-3'
    options = ['classic', 'candidate']


class SpotifyApplication(Snap):
    snap = 'spotify'
    options = []
