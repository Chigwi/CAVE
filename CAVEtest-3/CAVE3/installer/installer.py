import sys
import os
import shutil
from CAVE3.installer.distro import DistroChecker

class Installer:

    #initializes the class
    def __init__(self):
        #brings the distro checker
        self.distro = DistroChecker()
        #adds the path of where the ROMS are
        self.dest = os.path.expanduser('~/.config/retroarch/ROMS')

    #runs the processes in order
    def run(self):
        #checks the distro being used
        package_manager = self.distro.get_package_manager()
        #checks retroarch
        self._install_retroarch(package_manager)
        #installs the ROMS
        self._install_roms()

    # install retroarch
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


# main function installs ROMS from package
def _install_roms(self):

    # path where the ROMs are being stored in package
    source = self._resource_path('resources/ROMS')

    # path of where the ROMS should be saved for retroarch use
    print(f"Installing ROMS into {self.dest}")

    # clean install protocol
    if os.path.exists(self.dest):
        shutil.rmtree(self.dest)

    # moves the ROMS to target dir
    shutil.copytree(source,self.dest)

    # modifies the permissions of the ROM files
    os.system(f"chmod -R 755 '{self.dest}'")

    print("Installation complete")

def resource_path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)



