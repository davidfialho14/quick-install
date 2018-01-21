"""File containing all setting used by the tool"""
from quick_installer.applications import *

# Applications to be installed when performing a system install
SYSTEM_APPS = [
    SignalApplication,
    ChromeApplication,
    SeafileApplication,
    EnpassApplication,
    AtomApplication,
    SlackApplication,
    IntellijIDEAApplication,
    PyCharmApplication,
    SublimeApplication,
    SpotifyApplication
]
