
import shutil
import subprocess
import  sys
import os
import time

class RetroKiller:

    def safeStart(self):
        self._birthRetroarch()

    def safeStop(self):
        self._killRetroarch()

    def restart(self):
        self._killRetroarch()
        time.sleep(3)
        self._birthRetroarch()

    #kills the current retroarch process
    def _killRetroarch(self):
        if shutil.which('retroarch') is not None:
            print('Closing Retroarch')
            os.system('pkill retroarch')
        else:
            print ('Retroarch already closed, opening again')

    #births a new retroarch ´process
    def _birthRetroarch(self):
        print('Opening Retroarch')
        #popen makes sure it launches cleanly
        subprocess.Popen(['retroarch'])