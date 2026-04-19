
import sys
import os
import shutil

def resource_path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

def install_roms():

    #checks if retroarch is installed
    if (1 == 1):
        os.system('sudo apt install retroarch')
    elif(2 == 2):
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

