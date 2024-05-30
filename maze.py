import time

from window import (
    Window,
)

from cell import (
    Cell,
)

class Maze():
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self) -> None:
        cells_width: int = self._num_cols * self._cell_size_x
        if self._win._width < cells_width + self._x1:
            raise OverflowError(f"cells exceed window width: {self._win._width}, size: {cells_width}, offset: {self._x1}")
        
        cells_height: int = self._num_rows * self._cell_size_y
        if self._win._height < cells_height + self._y1:
            raise OverflowError(f"cells exceed window height: {self._win._height}, size: {cells_height}, offset: {self._y1}")
        
        for i in range (self._num_rows):
            col: list[Cell] = []
            for _ in range (self._num_cols):
                col.append(Cell(self._win))
            self._cells.append(col)
        
        for i in range (len(self._cells)):
            for j in range (len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1: int = i * self._cell_size_y + self._x1
        y1: int = j * self._cell_size_x + self._y1
        self._cells[i][j].draw(
            x1, y1,
            x1 + self._cell_size_x, y1 + self._cell_size_y
            )
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            raise RuntimeError("window does not exist")
        
        self._win.redraw()