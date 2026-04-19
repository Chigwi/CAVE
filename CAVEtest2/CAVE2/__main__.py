
import sys
import os
import shutil

def resource_path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

def install_roms():

    #checks if retroarch is installed
    if (os.system('cat /etc/os-release | grep ID') == "debian" or os.system('cat /etc/os-release | grep ID') == "ubuntu" or os.system('cat /etc/os-release | grep ID_LIKE') == "ubuntu debian"):
        os.system('sudo apt install retroarch')
    elif(os.system('cat /etc/os-release | grep ID') == "fedora" or os.system('cat /etc/os-release | grep ID_LIKE') == "fedora"):
        os.system('sudo dnf install retroarch')
    else:
        os.system('sudo pacman -S retroarch')

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

