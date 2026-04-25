
import sys
import os
import shutil
try:
    from installer.retrokiller import RetroKiller
except ImportError:
    from CAVE3.installer.retrokiller import RetroKiller
class Configuration:

    def __init__(self):
        # adds the path of where the config file is
        self.dest = os.path.expanduser('~/.config/retroarch/config')


    #runs the processes in order
    def run(self):
        #installs the configuration
        self._install_configuration()
        self.retroKiller = RetroKiller()


    #main function, installs the needed configuration onto the retroarch machine
    def _install_configuration(self):

        #path where the configuration are being stored in package
        source = self._resource_path('resources/config')

        #path of where the configuration should be saved for retroarch use
        print(f'Installing configuration into {self.dest}')

        #clean install protocol
        if os.path.exists(self.dest):
            shutil.rmtree(self.dest)

        #moves the configuration to the target dir
        shutil.copytree(source, self.dest)

        #modifies the permissions of the core files
        os.system(f"chmod -R 755  '{self.dest}'")

        print("config successfully installed ")

        os.system("retroarch -c ~/.config/retroarch/config/config.cfg | pkill retroarch")

        print('restarting...')
        self.retroKiller.restart()

        print("config set to config.cfg")

    def _resource_path(self, relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)