import logging

import time

from quick_installer import installers
from quick_installer.repository import Repository
from quick_installer.system import System

logger = logging.getLogger()
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def install_app(application_name: str, repository: Repository):
    try:
        application = repository.find_by_name(application_name)
    except KeyError:
        logger.error(f"Application '{application_name}' was not found")
        return

    if application.is_installed():
        logger.warning(f"'{application.name}' is already installed")
        return

    logger.info("Preparing...")
    application.setup(full=True)

    logger.info(f"Installing '{application.name}'...")
    application.install()

    logger.info(f"Cleaning up...")
    logger.info(f"Application '{application.name}' was install successfully!")


def install_system(repository: Repository):
    start_time = time.time()

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
    # Wait a little bit if the installation was too fast to avoid issues when apt-get
    # tries to get the lock
    if time.time() - start_time < 10:
        time.sleep(2)

    installers.apt.update()

    for app in non_installed_apps:
        logger.info(f"Installing '{app.name}'...'")
        app.install()

    logger.info("Cleaning up...")
    for app in non_installed_apps:
        app.cleanup()

    logger.info("System was installed successfully!")
