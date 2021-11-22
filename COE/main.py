import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window
from map.map import Map
from COE.camera.camera import Camera


def main(istest=False):
    window = Window()
    camera = Camera(window)
    map = Map()
    while window.get_loop():
        window.menu.loop = not istest
        window.show(map, camera, istest)


if __name__ == "__main__":
    main()
