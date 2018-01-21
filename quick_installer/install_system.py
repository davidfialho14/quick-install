import logging
from subprocess import CalledProcessError

from quick_installer import installers
from quick_installer.repository import Repository
from quick_installer.system import System

logger = logging.getLogger()
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def install_system():

    #
    # System Update
    #
    system = System()
    logger.info("Updating system...")
    system.update()
    logger.info("Cleaning up...")
    system.cleanup()
    logger.info("System is up-to-date!\n")

    #
    # Install applications
    #
    repository = Repository()

    for installer in installers.all():
        logger.info(f"Initializing '{installer.name}' installer...")
        installer.setup()

    all_apps = set(repository.system_apps())
    installed_apps = set(app for app in repository.system_apps() if app.is_installed())
    non_installed_apps = all_apps - installed_apps

    for app in installed_apps:
        logger.warning(f"'{app.name}' is already installed")

    if not non_installed_apps:
        logger.info("All apps are installed")
        return

    logger.info("Preparing installation...")
    for app in non_installed_apps:
        app.setup()

    logger.info("Checking repositories...")
    installers.apt.update()

    for app in non_installed_apps:
        logger.info(f"Installing '{app.name}'...'")

    logger.info("Cleaning up...")
    for app in non_installed_apps:
        app.cleanup()

    logger.info("System was installed successfully!")


def main():
    try:
        install_system()
    except CalledProcessError as error:
        print(str(error))


if __name__ == '__main__':
    main()