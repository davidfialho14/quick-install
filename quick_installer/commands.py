from docopt import docopt

from quick_installer.repository import Repository


def list():
    """
The list command lists all applications available through Quick Installer.

Usage:
  quickall list
"""
    docopt(str(list.__doc__))

    repository = Repository()

    print("APPLICATIONS")
    print("------------")
    for app in repository.all():
        print("-", app.name, "(Installed)" if app.is_installed() else "")
