from abc import ABC, abstractmethod
from subprocess import CalledProcessError
from typing import List

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
        cmd("apt-get update")

    def install(self, *packages: str):
        cmd("apt-get install -y " + " ".join(packages))

    def is_package_installed(self, package: str) -> bool:
        try:
            cmd(f"dpkg -s {package}")
            return True
        except CalledProcessError:
            return False


apt = AptInstaller()


def all() -> List[Installer]:
    return [apt]
