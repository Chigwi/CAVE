"""
myapp/__main__.py — Entry point of the application.

This works in two scenarios:
  1. Running directly in PyCharm (python __main__.py)
  2. Running from a packaged .pyz file (python3 myapp.pyz)

The image is read from inside the package using importlib.resources,
which is the Python equivalent of Java's getResourceAsStream().
"""

import io
import importlib.resources as pkg_resources
import tkinter as tk
from fileinput import filename

from PIL import Image, ImageTk


def load_image(package, filename):
    """
    Load an image from inside the package's resources folder.

    Java equivalent:
        InputStream is = getClass().getResourceAsStream("/images/cat.png");

    Python equivalent:
        with pkg_resources.open_binary("myapp.resources.images", "me-fr-cat.png") as f:

    The first argument is the dotted path to the folder INSIDE your package.
    Think of it like a Java package name:
        myapp/resources/images  →  "myapp.resources.images"

    The second argument is just the filename.

    """
    resource_path = pkg_resources.files(package).joinpath(filename)
    raw_bytes = resource_path.read_bytes()

    ##with pkg_resources.open_binary(package, filename) as f:
      ##  raw_bytes = f.read()
    return Image.open(io.BytesIO(raw_bytes))



def main():
    # Load the image from inside the package
    # "myapp.resources.images" is the dotted path to the images folder
    # "me-fr-cat.png" is the filename — change this to match yours

    img = load_image("myapp.resources.images", "me-fr-cat.png")

    # Standard tkinter window
    root = tk.Tk()
    root.title("CAVEtest1")
    root.resizable(False, False)

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo, bg="black")
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()