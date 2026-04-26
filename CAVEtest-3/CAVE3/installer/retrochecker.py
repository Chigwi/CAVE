
import sys
import os
import shutil
try:
    from installer.distro import DistroChecker
except ImportError:
    from CAVE3.installer.distro import DistroChecker

class RetroarchChecker:

    def __init__(self):
        self.distro = DistroChecker()


    # installs retroarch
    def install_retroarch(self, package_manager):
        # checks if retroarch is already installed
        if (shutil.which('retroarch') is not None):
            print('Retroarch executable found skipping installation')
            return
        # installs retroarch acording to the current distro
        elif (package_manager == 'apt'):
            os.system('sudo apt install -y retroarch')
        elif (package_manager == 'dnf'):
            os.system('sudo dnf install -y retroarch')
        elif (package_manager == 'pacman'):
            os.system('sudo pacman -S --noconfirm retroarch')

