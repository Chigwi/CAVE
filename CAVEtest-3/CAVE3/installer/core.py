
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

