
import sys
import os
import shutil
from CAVE3.installer.distro import DistroChecker
from CAVE3.installer.retrochecker import RetroarchChecker

class CoreInstaller:

    def __init__(self):
        # brings the distro checker
        self.distro = DistroChecker()
        #brings the retrochecker
        self.retrochecker = RetroarchChecker()
        # adds the path of where the ROMS are
        self.dest = os.path.expanduser('~/.config/retroarch/cores')


    #runs the processes in order
    def run(self):
        #checks the distro being used
        package_manager = self.distro.get_package_manager()
        #checks retroarch
        self.retrochecker.install_retroarch(package_manager)
        #installs the ROMS
        self._install_cores()


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

