import os
from abc import abstractmethod

from quick_installer.application import Application
from quick_installer.installers import apt, snap


class AptPackage(Application):

    @abstractmethod
    def soft_setup(self):
        pass

    def setup(self, full=False):
        self.soft_setup()
        if full:
            apt.update()


class SignalApplication(AptPackage):

    @property
    def name(self) -> str:
        return "signal"

    def soft_setup(self):
        apt.add_source(
            repository="deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main",
            name="signal",
            key_url="https://updates.signal.org/desktop/apt/keys.asc"
        )

    def install(self):
        apt.install('signal-desktop')

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return apt.is_package_installed('signal-desktop')


class ChromeApplication(AptPackage):

    @property
    def name(self) -> str:
        return "chrome"

    def soft_setup(self):
        apt.add_source(
            repository="deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main",
            name="google",
            key_url="https://dl-ssl.google.com/linux/linux_signing_key.pub"
        )

    def install(self):
        apt.install('google-chrome-stable')

    def cleanup(self):
        # The google installer creates an extra source file that causes warnings and errors
        # when updating system packages
        os.remove("/etc/apt/sources.list.d/google-chrome.list")

    def is_installed(self) -> bool:
        return apt.is_package_installed('google-chrome-stable')


class SeafileApplication(AptPackage):

    @property
    def name(self) -> str:
        return "seafile"

    def soft_setup(self):
        apt.add_ppa('ppa:seafile/seafile-client')

    def install(self):
        apt.install('seafile-gui')

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return apt.is_package_installed('seafile-gui')


class EnpassApplication(AptPackage):

    @property
    def name(self) -> str:
        return "seafile"

    def soft_setup(self):
        apt.add_source(
            repository="deb http://repo.sinew.in/ stable main",
            name="enpass",
            key_url="https://dl.sinew.in/keys/enpass-linux.key"
        )

    def install(self):
        apt.install('enpass')

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return apt.is_package_installed('enpass')


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
