
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
        self.retroKiller = RetroKiller()
        self.dest = os.path.expanduser('~/.config/retroarch/retroarch.cfg')
        self.source = self._resource_path('resources/config/retroarch.cfg')


    #runs the processes in order
    def run(self):
        #installs the configuration
        self._install_configuration()


    #main function, installs the needed configuration onto the retroarch machine
    def _install_configuration(self):
        #replaces og config with our config
        shutil.copy2(self.source, self.dest)
        #gives permissions
        os.system(f"chmod 744 '{self.dest}'")

    def _resource_path(self, relative):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, relative)