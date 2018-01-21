from quick_installer.application import Application
from quick_installer.installers import apt


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
