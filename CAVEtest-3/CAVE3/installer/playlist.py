import sys
import os
import shutil


class PlaylistInstaller:

    def __init__(self):
        # adds the path of where the playlists are
        self.dest = os.path.expanduser('~/.config/retroarch/playlists')

    def run(self):
        #installs playlists
        self._install_playlists()

    def _install_playlists(self):
        # path where the playlists are being stored in package
        source = self._resource_path('resources/playlists')

        # path of where the playlists should be saved for retroarch use
        print(f'Installing playlists into {self.dest}')

        # clean install protocol
        if os.path.exists(self.dest):
            shutil.rmtree(self.dest)

        # create destination folder
        os.makedirs(self.dest, exist_ok=True)

        # get actual home directory
        home = os.path.expanduser('~')

        # process each .lpl file replacing ~ with actual home path
        for filename in os.listdir(source):
            if filename.endswith('.lpl'):
                filepath = os.path.join(source, filename)
                with open(filepath, 'r') as f:
                    content = f.read()

                # replace ~ with actual home directory
                content = content.replace('~', home)

                dest_file = os.path.join(self.dest, filename)
                with open(dest_file, 'w') as f:
                    f.write(content)

        # modifies the permissions of the playlist files
        os.system(f"chmod -R 755 '{self.dest}'")

        print("Playlists successfully installed")

    def _resource_path(self, relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)