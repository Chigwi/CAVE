import os
import time

try:
    from installer.Rom import ROMInstaller
    from installer.core import CoreInstaller
    from installer.distro import DistroChecker
    from installer.playlist import PlaylistInstaller
    from installer.retrochecker import RetroarchChecker
    from installer.config import Configuration
    from installer.retrokiller import RetroKiller
except ImportError:
    from CAVE3.installer.Rom import ROMInstaller
    from CAVE3.installer.core import CoreInstaller
    from CAVE3.installer.distro import DistroChecker
    from CAVE3.installer.playlist import PlaylistInstaller
    from CAVE3.installer.retrochecker import RetroarchChecker
    from CAVE3.installer.config import Configuration
    from CAVE3.installer.retrokiller import RetroKiller


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
        #brings the relevant configuration
        self.configInstaller = Configuration()
        #brings the retrokiller tool
        self.retrokiller = RetroKiller()


    def install(self):
        #checks the distro
        distro = self.distro.get_package_manager()
        #installs retroarch first
        self.checker.install_retroarch(distro)
        #proceeds with the installation in optimal order
        self.coreInstaller.run()
        self.romInstaller.run()
        self.playlistInstaller.run()

        print('abre retroarch para crear archivo .cfg')
        self.retrokiller.safeStart()
        time.sleep(5)
        print ('cierra retroarch')
        self.retrokiller.safeStop()

        print('instala nuevo archivo .cfg')
        self.configInstaller.run()

        print('abre y reinicia')
        self.retrokiller.safeStart()
        self.retrokiller.restart()