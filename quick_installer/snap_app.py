from quick_installer.app import Application
from quick_installer.installers import snap


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