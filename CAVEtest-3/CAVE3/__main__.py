import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from installer.installationManager import InstallationManager

if __name__ == "__main__":
    manager = InstallationManager()
    manager.install()
