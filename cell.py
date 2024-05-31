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
        self.visited: bool = False
    
    def draw(
            self, x1: int, y1: int, x2: int, y2: int,
            fill_color: str = "black") -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        left_wall = Line(
            Point(self._x1, self._y1),
            Point(self._x1, self._y2)
            )
        if self.has_left:
            self._win.draw_line(left_wall, fill_color)
        else:
            self._win.draw_line(left_wall, self._win._background_color)
        
        right_wall = Line(
            Point(self._x2, self._y1),
            Point(self._x2, self._y2)
            )
        if self.has_right:
            self._win.draw_line(right_wall, fill_color)
        else:
            self._win.draw_line(right_wall, self._win._background_color)
        
        top_wall = Line(
            Point(self._x1, self._y1),
            Point(self._x2, self._y1)
            )
        if self.has_top:
            self._win.draw_line(top_wall, fill_color)
        else:
            self._win.draw_line(top_wall, self._win._background_color)

        bottom_wall = Line(
            Point(self._x1, self._y2),
            Point(self._x2, self._y2)
            )
        if self.has_bottom:
            self._win.draw_line(bottom_wall, fill_color)
        else:
            self._win.draw_line(bottom_wall, self._win._background_color)
    
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