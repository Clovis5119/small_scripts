from PIL import Image
import os


def resize(img, w):
    """
    Resizes an image while preserving its aspect ratio.

    TODO: Accept either width or length parameter and resize based on the
     one provided.

    :param img: image to resize
    :param w: desired width
    """
    w_percent = (w / float(img.size[0]))
    new_height = int((float(img.size[1]) * float(w_percent)))
    return img.resize((w, new_height), Image.LANCZOS)


width = 1000                            # Desired width
path = "D:/Kurt/Downloads/images/"      # Location of the images

for item in os.listdir(path):
    im = Image.open(path+item)
    print(f"Resizing {item}", end="... ")
    resize(im, width).save(path+item, 'JPEG', quality=90)
    print("Done.")

print("\nAll jobs done!")
