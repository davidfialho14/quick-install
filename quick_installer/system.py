import subprocess


class System:
    OPTIONS = "-yqq --show-progress -o Dpkg::Progress-Fancy=true"

    def update(self):
        cmd(f"apt-get update -qq")
        cmd(f"apt-get upgrade {self.OPTIONS}")

    def cleanup(self):
        cmd(f"apt-get autoremove {self.OPTIONS}")


def cmd(command: str):
    subprocess.run(command.split(" "), check=True)
