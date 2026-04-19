
import sys
import os
import shutil
import subprocess

#creates the resource relative path to the ROMS packaged inside
def resource_path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

#checks the current linux distro
def check_disto():
    #rcieves the output containing the current distro
    retorno = subprocess.run(['cat', '/etc/os-release'], capture_output =True, text = True)
    #lower case xd
    output = retorno.stdout.lower()
    #checks the output to see which distro is current and returns
    if ('debian' in output or 'ubuntu' in output):
        return 'apt'
    elif('fedora' in output):
        return 'dnf'
    else:
        return 'pacman'

#install retroarch
def install_retroarch(distro):
    #checks if retroarch is already installed
    if (shutil.which('retroarch') is not None):
        print('spp: Sub Proseso de Paso')
        return
    #installs retroarch acording to the current distro
    elif (distro == 'apt'):
        os.system('sudo apt install retroarch')
    elif (distro == 'dnf'):
        os.system('sudo dnf install retroarch')
    elif (distro == 'pacman'):
        os.system('sudo pacman -S retroarch')
    

#main function installs ROMS from package
def install_roms():
    #checks distro
    distro = check_disto()

    #installs retroarch
    install_retroarch(distro)

    #path where the ROMs are being stored in package
    source = resource_path('resources/ROMS')

    #path of where the ROMS should be saved for retroarch use
    dest = os.path.expanduser('~/.config/retroarch/ROMS')

    print(f"Installing ROMS into {dest}")

    #clean install protocol
    if os.path.exists(dest):
        shutil.rmtree(dest)

    #moves the ROMS to target dir
    shutil.copytree(source, dest)

    #modifies the permissions of the ROM files
    os.system(f"chmod -R 755 '{dest}'")

    print("Installation complete")

if __name__ == "__main__":
    install_roms()

