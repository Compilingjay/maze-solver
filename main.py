from window import (
    Window,
)

from maze import (
    Maze,
)


def main():
    win = Window(800, 800)
    maze = Maze(4, 4, 6, 6, 40, 40, win)
    win.wait_for_close()


main()
