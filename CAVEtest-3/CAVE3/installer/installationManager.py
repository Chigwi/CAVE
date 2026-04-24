import os

from CAVE3.installer.Rom import ROMInstaller
from CAVE3.installer.core import CoreInstaller
from CAVE3.installer.distro import DistroChecker
from CAVE3.installer.playlist import PlaylistInstaller
from CAVE3.installer.retrochecker import RetroarchChecker


class InstallationManager:

    def __init__(self):
        #brings the new distrochecker
        self.distro = DistroChecker()
        #birngs the new retrochecker
        self.checker = RetroarchChecker()
        #brings the new rominstaller
        self.romInstaller = ROMInstaller()
        #brings the new coreinstaller
        self.coreInstaller = CoreInstaller()
        #brings the new plinstaller
        self.playlistInstaller = PlaylistInstaller()

    def install(self):
        #checks the distro
        distro = self.distro.get_package_manager()
        #installs retroarch first
        self.checker.install_retroarch(distro)
        #proceeds with the installation in optimal order
        self.coreInstaller.run()
        self.romInstaller.run()
        self.playlistInstaller.run()
        #opens retroarch
        os.system('retroarch')
