from COE.UI.window_ui import Window
from COE.map.map import Map


def main(istest=False):
    window = Window()
    map = Map()
    while window.get_loop():
        window.menu.loop = not istest
        window.show(map, istest)


if __name__ == "__main__":
    main()
