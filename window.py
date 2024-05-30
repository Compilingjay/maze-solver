from tkinter import (
    Tk,
    BOTH,
    Canvas
)


class Window():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack(expand=True)
        self.run = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.run = True
        while self.run:
            self.redraw()
    
    def close(self):
        self.run = False
    
    def draw_line(self, line, fill_color: str = "black"):
        line.draw(self.canvas, fill_color)
