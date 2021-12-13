import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

from UI.window_ui import Window


def main():
    window = Window()
    while window.get_loop():
        window.show()


if __name__ == "__main__":
    main()
