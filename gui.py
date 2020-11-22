import pygame
import block as b
import grid as g
import pathfinder as p
from tkinter import *
from tkinter import messagebox

# INIT PYGAME
pygame.init()

# SIZE VARIABLES
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 800
BLOCK_SIZE = 20

win = None
pencil = None
grid = None


def main():
    global win, pencil, grid

    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    win.fill((87, 89, 93))

    pygame.display.set_caption("A*")

    pygame.font.init()

    pencil = b.BlockType.WALL

    grid_ = g.Grid(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)
    grid = grid_.grid
    run = True
    started = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if not started:
                if pygame.mouse.get_pressed()[0]:
                    for col in grid:
                        for value in col:
                            rect = value.get_rect()
                            if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                                if pencil == b.BlockType.START:
                                    found, block = grid_.start_or_end_found(b.BlockType.START)
                                    if found:
                                        block.set_default()
                                    value.set_start()
                                elif pencil == b.BlockType.END:
                                    found, block = grid_.start_or_end_found(b.BlockType.END)
                                    if found:
                                        block.set_default()
                                    value.set_end()
                                else:
                                    value.set_wall()

                elif pygame.mouse.get_pressed()[2]:
                    for col in grid:
                        for value in col:
                            rect = value.get_rect()
                            if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                                value.set_default()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        pencil = b.BlockType.START
                    if event.key == pygame.K_F2:
                        pencil = b.BlockType.END
                    if event.key == pygame.K_F3:
                        pencil = b.BlockType.WALL
                    if event.key == pygame.K_SPACE:
                        if not grid_.find_start() is None and not grid_.find_end() is None:
                            started = True
                            a_star = p.Pathfinder(grid_)
                            a_star.find_path(lambda: grid_.draw_grid(win, b.type_color), grid_.find_start(), grid_.find_end())
                        else:
                            Tk().wm_withdraw()  # to hide the main window
                            messagebox.showinfo('ERROR', 'Please select a starting and end point')

        win.fill((87, 89, 93))
        grid_.draw_grid(win, b.type_color)


main()
