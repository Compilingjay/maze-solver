import random

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
            win: Window,
            seed: int | float | str | bytes | bytearray | None = None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_recursive()
        self._reset_cells_visited()
    
    def _create_cells(self) -> None:
        if not self._win:
            raise ValueError("maze window does not exist")
        cells_width: int = self._num_cols * self._cell_size_x
        if self._win._width < cells_width + self._x1:
            raise OverflowError(
                f"maze cells exceed window width: \
                {self._win._width}, size: {cells_width}, offset: {self._x1}")
        cells_height: int = self._num_rows * self._cell_size_y
        if self._win._height < cells_height + self._y1:
            raise OverflowError(
                f"maze cells exceed window height: \
                {self._win._height}, size: {cells_height}, offset: {self._y1}")
        
        for i in range (self._num_cols):
            col: list[Cell] = []
            for _ in range (self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        
        for i in range (self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1: int = i * self._cell_size_x + self._x1
        y1: int = j * self._cell_size_y + self._y1
        self._cells[i][j].draw(
            x1, y1,
            x1 + self._cell_size_x, y1 + self._cell_size_y
            )
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            raise RuntimeError("window does not exist")
        
        self._win.redraw()
    
    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols-1, self._num_rows-1)
    
    def _break_walls_recursive(self, i: int = 0, j: int = 0) -> None:
        directions: list[(int, int, str)] = []
        if i > 0 and not self._cells[i-1][j].visited:
            directions.append((i-1, j, "left"))
        if j > 0 and not self._cells[i][j-1].visited:
            directions.append((i, j-1, "up"))
        if i + 1 < self._num_cols and not self._cells[i+1][j].visited:
            directions.append((i+1, j, "right"))
        if j + 1 < self._num_rows and not self._cells[i][j+1].visited:
            directions.append((i, j+1, "down"))
        
        directions_rem = len(directions)
        while directions_rem > 0:
            k: int = random.randint(0, directions_rem - 1)
            dir: set[int, int, str] = directions.pop(k)
            directions_rem -= 1

            match dir[2]:
                case "left":
                    self._break_wall_visited(dir[0], dir[1], "right")
                case "right":
                    self._break_wall_visited(dir[0], dir[1], "left")
                case "up":
                    self._break_wall_visited(dir[0], dir[1], "down")
                case "down":
                    self._break_wall_visited(dir[0], dir[1], "up")
            self._break_walls_recursive(dir[0], dir[1])
    
    def _break_wall_visited(self, i: int, j: int, direction: str) -> None:
        if self._cells[i][j].visited:
            return
        
        self._cells[i][j].visited = True
        match direction:
            case "left":
                self._cells[i][j].has_left = False
            case "right":
                self._cells[i][j].has_right = False
            case "up":
                self._cells[i][j].has_top = False
            case "down":
                self._cells[i][j].has_bottom = False
        self._draw_cell(i, j)
    
    def _reset_cells_visited(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def _solve(self, i: int = 0, j: int = 0):
        return self._solve_recursive_dfs(i, j)

    def _solve_recursive_dfs(self, i: int, j: int):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if (not i - 1 < 0 
                and not self._cells[i-1][j].visited
                and not self._cells[i-1][j].has_right):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_recursive_dfs(i-1, j):
                return True

            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        if (not j - 1 < 0 
                and not self._cells[i][j-1].visited
                and not self._cells[i][j-1].has_bottom):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_recursive_dfs(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        
        if (not i + 1 >= self._num_cols
                and not self._cells[i+1][j].visited
                and not self._cells[i+1][j].has_left):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_recursive_dfs(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        
        if (not j + 1 >= self._num_rows
                and not self._cells[i][j+1].visited
                and not self._cells[i][j+1].has_top):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_recursive_dfs(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        return False