from COE.UI.window_ui import Window
from COE.map.map import Map
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
