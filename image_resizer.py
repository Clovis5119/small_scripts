"""
TODO: Use pathlib Path to open files instead of os
"""

from PIL import Image
import os


def run_program():
    """
    Executes the main script.

    - Iterate over each <item> in the given <PATH>
    - Create a new <Image> object for each item
    - Call the <resize_image()> method on each object

    TODO: Error handling for items that are not images.
    """
    for item in os.listdir(PATH):
        filename = PATH + item
        with Image.open(filename) as im:
            print(f"Resizing ::  {item}", end=" ::  ")
            resize_image(im, LENGTH, s=SIDE).save(filename, 'JPEG', quality=90)
            print("done")

    print("\nAll jobs done!")


def resize_image(img, n, s=None):
    """
    Resizes an image while preserving its aspect ratio.

    TODO: Add option to print before & after dimensions
    TODO: Contain imports within functions?

    :param img: image to resize
    :param n: new length of <s>
    :param s: 'width' or 'height'
    """
    old_w, old_h = analyze_image(img)

    if s == 'width':
        ratio = n / old_w
        new_h = int(old_h * ratio)
        return img.resize((n, new_h), Image.LANCZOS)

    elif s == 'height':
        ratio = n / old_h
        new_w = int(old_w * ratio)
        return img.resize((new_w, n), Image.LANCZOS)

    else:
        return img


def analyze_image(img):
    """
    Analyzes the width and height of an image.

    :param img: image to analyze
    :return: (width, height)
    """
    return img.size[0], img.size[1]


"""       *  CONFIG SETTINGS  *       """

PATH = "D:/Kurt/Downloads/images/"      # Location of the images
SIDE = 'width'                          # Change width or height?
LENGTH = 1000                           # New length of the chosen side

"""       *  CONFIG SETTINGS  *       """

run_program()
