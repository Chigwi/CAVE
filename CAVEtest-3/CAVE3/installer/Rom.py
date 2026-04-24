import sys
import os
import shutil


class ROMInstaller:

    #initializes the class
    def __init__(self, distro, checker):
        #brings the distro checker
        self.distro = distro
        #brings the retrochecker
        self.retrochecker = checker
        #adds the path of where the ROMS are
        self.dest = os.path.expanduser('~/.config/retroarch/ROMS')

    #runs the processes in order
    def run(self):
        #checks the distro being used
        package_manager = self.distro.get_package_manager()
        #checks retroarch
        self.retrochecker.install_retroarch(package_manager)
        #installs the ROMS
        self._install_roms()



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

    def _resource_path(self, relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)



