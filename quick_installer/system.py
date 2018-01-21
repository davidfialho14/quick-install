import subprocess


class System:

    def update(self):
        cmd("apt-get update")
        cmd("apt-get upgrade")

    def cleanup(self):
        cmd("apt-get autoremove")


def cmd(command: str) -> str:
    process = subprocess.run(command.split(" "), stdout=subprocess.PIPE, check=True)
    return process.stdout.decode()
