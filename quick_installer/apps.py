from quick_installer.apt_app import AptPackage, Source
from quick_installer.snap_app import Snap


class SignalApplication(Snap):
    name = 'signal'
    snap = "signal-desktop"
    options = []


class ChromeApplication(AptPackage):
    name = "chrome"
    package = 'google-chrome-stable'
    source = Source(
        repository="deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main",
        name="google-chrome",
        key_url="https://dl-ssl.google.com/linux/linux_signing_key.pub"
    )


class SeafileApplication(AptPackage):
    name = "seafile"
    package = 'seafile-gui'


class EnpassApplication(AptPackage):
    name = "enpass"
    package = 'enpass'
    source = Source(
        repository="deb http://repo.sinew.in/ stable main",
        name="enpass",
        key_url="https://dl.sinew.in/keys/enpass-linux.key"
    )


class AtomApplication(Snap):
    snap = 'atom'
    options = ['classic']


class SlackApplication(Snap):
    snap = 'slack'
    options = ['classic']


class IntellijIDEAApplication(Snap):
    snap = 'intellij-idea-community'
    options = ['classic']


class PyCharmApplication(Snap):
    snap = 'pycharm-community'
    options = ['classic']


class SublimeApplication(Snap):
    name = 'sublime'
    snap = 'sublime-text'
    options = ['classic', 'candidate']


class SpotifyApplication(Snap):
    snap = 'spotify'
    options = []
