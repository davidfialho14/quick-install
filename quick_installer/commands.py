from subprocess import CalledProcessError

from docopt import docopt

from quick_installer.install import install_system, install_app
from quick_installer.repository import Repository


def list(repository: Repository):
    """
The list command lists all applications available through Quick Installer.

Usage:
  quickall list
"""
    docopt(str(list.__doc__))

    print("APPLICATIONS")
    print("------------")
    for app in repository.all():
        print("-", app.name, "(Installed)" if app.is_installed() else "")


def system(repository: Repository):
    """
The system command performs a system installation.

Usage:
  quickall system
"""
    docopt(str(system.__doc__))

    # TODO ensure sudo

    try:
        install_system(repository)
    except CalledProcessError as error:
        print(str(error))


def install(repository: Repository):
    """
The install command install the specified application.

Usage:
  quickall install <application>
"""
    args = docopt(str(install.__doc__))
    application_name = args['<application>']

    # TODO ensure sudo

    try:
        install_app(application_name, repository)
    except CalledProcessError as error:
        print(str(error))
