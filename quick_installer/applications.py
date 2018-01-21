import os

from quick_installer.application import Application
from quick_installer.installers import apt, snap


class SignalApplication(Application):

    @property
    def name(self) -> str:
        return "signal"

    def setup(self):
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


class ChromeApplication(Application):

    @property
    def name(self) -> str:
        return "chrome"

    def setup(self):
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


class SeafileApplication(Application):

    @property
    def name(self) -> str:
        return "seafile"

    def setup(self):
        apt.add_ppa('ppa:seafile/seafile-client')

    def install(self):
        apt.install('seafile-gui')

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return apt.is_package_installed('seafile-gui')


class AtomApplication(Application):

    @property
    def name(self) -> str:
        return "atom"

    def setup(self):
        pass

    def install(self):
        snap.install('atom', options=['classic'])

    def cleanup(self):
        pass

    def is_installed(self) -> bool:
        return snap.is_snap_installed('atom')
