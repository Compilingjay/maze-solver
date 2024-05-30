from tkinter import (
    Canvas,
)


class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1: Point, point2: Point) -> None:
        self.p1: Point = point1
        self.p2: Point = point2
    

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
            )
