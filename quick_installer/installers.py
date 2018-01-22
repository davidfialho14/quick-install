from abc import ABC, abstractmethod
from subprocess import CalledProcessError
from typing import List

import os

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
        cmd(f"apt-add-repository -y {ppa_repository}")

    def add_source(self, repository: str, name: str, key_url: str):
        cmd(f"curl -s {key_url} | apt-key add -")
        cmd(f"echo \"{repository}\" | tee -a /etc/apt/sources.list.d/{name}.list")

    def update(self):
        cmd("apt-get update -qq")

    def install(self, *packages: str):
        cmd("apt-get install -yqq --show-progress -o Dpkg::Progress-Fancy=true " + " ".join(packages))

    def is_package_installed(self, package: str) -> bool:
        try:
            cmd(f"dpkg -s {package}")
            return True
        except CalledProcessError:
            return False


# noinspection PyMethodMayBeStatic
class SnapInstaller(Installer):

    @property
    def name(self) -> str:
        return "Snap"

    def setup(self):
        apt.install('snapd', 'snap')

    def install(self, snap: str, options: List[str]):
        command = f"snap install {snap}"
        if options:
            command += " " + " ".join(f"--{option}" for option in options)

        cmd(command)

    def is_snap_installed(self, snap: str) -> bool:
        return os.path.exists(f"/snap/{snap}")


apt = AptInstaller()
snap = SnapInstaller()


def all() -> List[Installer]:
    return [apt, snap]
