
import sys
import os
import shutil
import subprocess

def resource_path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

def check_disto():

    retorno = subprocess.run(['cat', '/etc/os-release'], capture_output == true, text == true)
    output = retorno.stdout.lower()
    #checks if retroarch is installed
    if ('debian' in output or 'ubuntu' in output):
        return 'apt'
    elif('fedora' in output):
        return 'dnf'
    else:
        return 'pacman'

def install_retroarch(distro):
    if (shutil.which('retroarch') is not None):
        print('spp: Sub Proseso de Paso')
        return
    elif (distro == 'apt'):
        os.system('sudo apt install retroarch')
    elif (distro == 'dnf'):
        os.system('sudo dnf install retroarch')
    elif (distro == 'pacman'):
        os.system('sudo pacman -S retroarch')
    

def install_roms():

    distro = check_disto()
    install_retroarch(distro)
    #path where the ROMs are being stored
    source = resource_path('resources/ROMS')

    #path of where the ROMS should be saved for retroarch use
    dest = os.path.expanduser('~/.config/retroarch/ROMS')

    print(f"Installing ROMS into {dest}")

    #clean install protocol
    if os.path.exists(dest):
        shutil.rmtree(dest)


    shutil.copytree(source, dest)

    os.system(f"chmod -R 755 '{dest}'")

    print("Installation complete")

if __name__ == "__main__":
    install_roms()

