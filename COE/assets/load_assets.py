"""
Load the images used inside the game
"""
import glob
from pygame import image

images = glob.glob("*.png")

image_cache = {}


def get_image(key):
    key = key[:-4]  # Getting rid of the .png, .jpg or .bmp
    if key not in image_cache:
        image_cache[key] = image.load(key)
    return image_cache[key]


for image in images:
    get_image(image)
