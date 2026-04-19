
import os

def main():
    print("Hello World")

    if (1 == 1):
        os.system('sudo apt install retroarch')
    elif(2 == 2):
        os.system('sudo dnf install retroarch')
    else:
        os.system('sudo pacman -S retroarch')
    os.system('mkdir ~/.config/retroarch/ROMS')
    os.system('cp -r ROMS ~/.config/retroarch/ROMS')