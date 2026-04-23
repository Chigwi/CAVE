
import sys
import os
import shutil
from CAVE3.installer.distro import DistroChecker

class CoreInstaller:

    def __init__(self):
        # brings the distro checker
        self.distro = DistroChecker()
        # adds the path of where the ROMS are
        self.dest = os.path.expanduser('~/.config/retroarch/cores')

# install retroarch, hopefully dead code as retroarch should already be installed
    def _install_retroarch(self, package_manager):
            # checks if retroarch is already installed
            if (shutil.which('retroarch') is not None):
                print('Retroarch executable found skipping installation')
                return
            # installs retroarch acording to the current distro
            elif (package_manager == 'apt'):
                os.system('sudo apt install retroarch')
            elif (package_manager == 'dnf'):
                os.system('sudo dnf install retroarch')
            elif (package_manager == 'pacman'):
                os.system('sudo pacman -S retroarch')


    #main function, installs the needed cores onto the retroarch machine
    def _install_cores(self):

        #path where the cores are being stored in package
        source = self._source_path('resources/cores')

        #path of where the cores should be saved for retroarch use
        print(f'Installing cores into {self.dest}')

        #clean install protocol
        if os.path.exists(self.dest):
            shutil.rmtree(self.dest)

        #moves the cores to the target dir
        shutil.copytree(source, self.dest)

        #modifies the permissions of the core files
        os.system(f"chmod -R 755  '{self.dest}'")

        print("Cores successfully installed")

    def resource_path(relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)

