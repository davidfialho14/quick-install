import os
import shutil
from abc import ABC, abstractmethod
from subprocess import CalledProcessError
from tempfile import mkstemp
from typing import List
from urllib.request import urlopen

from quick_installer.system import cmd


class Installer(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def setup(self):
        pass


# noinspection PyMethodMayBeStatic
class AptInstaller(Installer):

    @property
    def name(self) -> str:
        return "APT"

    def setup(self):
        self.install('software-properties-common')

    def add_ppa(self, ppa_repository: str):
        cmd(f"apt-add-repository -y {ppa_repository}", silent=True)

    def add_source(self, repository: str, name: str, key_url: str):
        # Download key file to a temporary file
        _, key_tempfile = mkstemp()
        with urlopen(key_url) as response, open(key_tempfile, "wb") as key_file:
            shutil.copyfileobj(response, key_file)

        try:
            # Register the key
            cmd(f"apt-key add {key_tempfile}", silent=True)
        finally:
            os.remove(key_tempfile)

        with open(f"/etc/apt/sources.list.d/{name}.list", "w") as source_file:
            source_file.write(repository)

    def update(self):
        cmd("apt-get update -qq")

    def install(self, *packages: str):
        cmd("apt-get install -yqq --show-progress -o Dpkg::Progress-Fancy=true " + " ".join(
            packages))

    def is_package_installed(self, package: str) -> bool:
        try:
            cmd(f"dpkg -s {package}", silent=True)
            return True
        except CalledProcessError:
            return False


class SnapInstaller(Installer):

    @property
    def name(self) -> str:
        return "Snap"

    def setup(self):
        apt.install('snapd', 'snap')

    def install(self, snap_name: str, options: List[str]):
        command = f"snap install {snap_name}"
        if options:
            command += " " + " ".join(f"--{option}" for option in options)

        cmd(command)

    def is_snap_installed(self, snap_name: str) -> bool:
        return os.path.exists(f"/snap/{snap_name}")


apt = AptInstaller()
snap = SnapInstaller()


def all() -> List[Installer]:
    return [apt, snap]
