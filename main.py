from window import (
    Window,
)

from maze import (
    Maze,
)


def main():
    win = Window(800, 800)
    maze = Maze(4, 4, 7, 6, 40, 40, win)
    if maze._solve():
        print("maze solved!")
    else:
        print("No solution to the maze")
    
    win.wait_for_close()

main()
