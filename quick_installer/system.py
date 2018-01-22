import subprocess


class System:
    OPTIONS = "-yqq --show-progress -o Dpkg::Progress-Fancy=true"

    def update(self):
        cmd(f"apt-get update -qq")
        cmd(f"apt-get dist-upgrade {self.OPTIONS}")

    def cleanup(self):
        cmd(f"apt-get autoremove {self.OPTIONS}")


def cmd(command: str, silent=False):
    stdout = stderr = None

    if silent:
        stdout = stderr = subprocess.DEVNULL

    subprocess.run(command.split(" "), stderr=stderr, stdout=stdout, check=True)
