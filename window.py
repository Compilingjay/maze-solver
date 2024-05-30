from tkinter import (
    Tk,
    BOTH,
    Canvas
)

from drawable import (
    Line,
)


class Window():
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(width=self._width, height=self._height)
        self.__canvas.pack(expand=True)
        self.__run = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__run = True
        while self.__run:
            self.redraw()
    
    def close(self):
        self.__run = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.__canvas, fill_color)
