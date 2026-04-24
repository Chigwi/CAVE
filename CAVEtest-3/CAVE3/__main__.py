import sys
import os

# makes sure the CAVE3 package is always findable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CAVE3.installer.installationManager import InstallationManager
#main function runs the installer
if __name__ == "__main__":
    manager = InstallationManager()
    manager.install()
