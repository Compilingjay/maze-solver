from window import (
    Window,
)

from drawable import (
    Point,
    Line,
)

from cell import (
    Cell,
)


def main():
    win = Window(800, 800)
    p1 = Point(200, 200)
    p2 = Point(400, 500)
    line = Line(p1, p2)
    win.draw_line(line, "black")
    cell = Cell(win)
    cell._win = win
    cell.draw(p1.x, p1.y, p2.x, p2.y)
    win.wait_for_close()


main()
