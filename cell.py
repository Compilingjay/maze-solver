from window import (
    Window,
)

from drawable import (
    Point,
    Line
)


class Cell():
    def __init__(self, win: Window) -> None:
        self.has_left:   bool = True
        self.has_right:  bool = True
        self.has_top:    bool = True
        self.has_bottom: bool = True
        self._x1: int = None
        self._y1: int = None
        self._x2: int = None
        self._y2: int = None
        self._win = win
    
    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left:
            left_wall = Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
                )
            self._win.draw_line(left_wall)
        if self.has_right:
            right_wall = Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
                )
            self._win.draw_line(right_wall)
        if self.has_top:
            top_wall = Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
                )
            self._win.draw_line(top_wall)        
        if self.has_bottom:
            bottom_wall = Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
                )
            self._win.draw_line(bottom_wall)
    
    def draw_move(self, to_cell: object, undo=False):
        path_color: str
        if undo:
            path_color = "red"
        else:
            path_color = "gray"

        path = Line(
            Point(
                (self._x1 + self._x2) / 2,
                (self._y1 + self._y2) / 2),   
            Point(
                (to_cell._x1 + to_cell._x2) / 2,
                (to_cell._y1 + to_cell._y2) / 2)
            )
        self._win.draw_line(path, path_color)