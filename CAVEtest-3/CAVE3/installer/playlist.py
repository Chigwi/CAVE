
import sys
import os
import shutil


class PlaylistInstaller:

    def __init__(self, distro, checker):
        # brings the distro checker
        self.distro = distro
        # brings the retrochecker
        self.retrochecker = checker
        # adds the path of where the ROMS are
        self.dest = os.path.expanduser('~/.config/retroarch/playlists')


    def run(self):
        #checks the distro being used
        package_manager = self.distro.get_package_manager()
        #checks retroarch
        self.retrochecker.install_retroarch(package_manager)
        #installs playlists
        self._install_playlists()

    def _install_playlists(self):
        # path where the cores are being stored in package
        source = self._resource_path('resources/playlists')

        # path of where the playlists should be saved for retroarch use
        print(f'Installing playlists into {self.dest}')

        # clean install protocol
        if os.path.exists(self.dest):
            shutil.rmtree(self.dest)

        # moves the cores to the target dir
        shutil.copytree(source, self.dest)

        # modifies the permissions of the core files
        os.system(f"chmod -R 755  '{self.dest}'")

        print("Playlists successfully installed")

    def _resource_path(self, relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)