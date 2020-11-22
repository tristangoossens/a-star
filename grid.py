import block as b
import pygame


class Grid:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.rows = width // size
        self.cols = height // size
        self.block_size = size
        self.grid = self.create_grid()
        self.currentBlock = self.grid[0][0]

    def create_grid(self):
        grid = []
        for y in range(self.cols):
            row = []
            for x in range(self.rows):
                item = b.Block(x, y, self.block_size)
                row.append(item)

            grid.append(row)
        return grid

    def get_neighbours(self, block):
        neighbours = []

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                else:
                    check_x = block.row + x
                    check_y = block.col + y

                    if check_x >= 0 and check_x < self.rows and check_y >= 0 and check_y < self.cols:
                        neighbours.append(self.grid[check_y][check_x])

        return neighbours

    def draw_grid(self, win, switch):
        for col in range(len(self.grid)):
            for row in range(len(self.grid[0])):
                self.grid[col][row].draw(win, switch.get(self.grid[col][row].type))

        for x in range(0, self.width, self.block_size):
            pygame.draw.line(win, [212, 212, 212], (x, 0), (x, self.height))
            for y in range(0, self.height, self.block_size):
                pygame.draw.line(win, [212, 212, 212], (0, y), (self.width, y))

        pygame.draw.line(win, [212, 212, 212], (self.width, 0), (self.width, self.height))

        pygame.display.update()

    def start_or_end_found(self, block_type):
        for col in self.grid:
            for value in col:
                if value.type == block_type:
                    return True, value

        return False, None

    def find_start(self):
        for col in self.grid:
            for value in col:
                if value.type == b.BlockType.START:
                    return value.row, value.col

        return None

    def find_end(self):
        for col in self.grid:
            for value in col:
                if value.type == b.BlockType.END:
                    return value.row, value.col

        return None
