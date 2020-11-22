import pygame
from enum import Enum


class BlockType(Enum):
    DEFAULT = 1
    WALL = 2
    START = 3
    END = 4
    OPEN = 5
    CLOSED = 6
    PATH = 7


type_color = {
    BlockType.DEFAULT: [87, 89, 93],
    BlockType.WALL: [0, 0, 0],
    BlockType.START: [24, 71, 24],
    BlockType.END: [88, 45, 45],
    BlockType.OPEN: [0, 255, 0],
    BlockType.CLOSED: [255, 0, 0],
    BlockType.PATH: [39, 41, 80],
}


class Block:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.type = BlockType.DEFAULT

        self.gCost = 0
        self.hCost = 0
        self.parent = None

        self.rect = pygame.Rect(self.x, self.y, width, width)

    def get_rect(self):
        return self.rect

    def set_default(self):
        self.type = BlockType.DEFAULT

    def set_wall(self):
        self.type = BlockType.WALL

    def set_start(self):
        self.type = BlockType.START

    def set_end(self):
        self.type = BlockType.END

    def set_closed(self):
        self.type = BlockType.CLOSED

    def set_open(self):
        self.type = BlockType.OPEN

    def set_path(self):
        self.type = BlockType.PATH

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rect)

    def f_cost(self):
        return self.gCost + self.hCost
