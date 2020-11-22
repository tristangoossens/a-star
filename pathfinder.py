import block as b
import time


class Pathfinder:
    def __init__(self, grid):
        self.grid_object = grid
        self.grid = grid.grid

    @staticmethod
    def get_distance(block_a, block_b):
        dist_x = abs(block_a.x - block_b.x)
        dist_y = abs(block_a.y - block_b.y)

        if dist_x > dist_y:
            return 14*dist_y + 10*(dist_x-dist_y)

        return 14 * dist_x + 10 * (dist_y - dist_x)

    def retrace_path(self, start, end):
        path = []
        current_block = end

        while not current_block == start:
            path.append(current_block)
            current_block = current_block.parent

        path.append(start)

        path.reverse()

        for block in path:
            block.set_path()

        # OPTIONAL REMOVE OPEN AND CLOSED BLOCKS AFTER FINDING PATH
        self.show_path()

    def show_path(self):
        for row in self.grid:
            for block in row:
                if block.type == b.BlockType.OPEN or block.type == b.BlockType.CLOSED:
                    block.set_default()

    def find_path(self, draw, start, end):
        start_block = self.grid[start[1]][start[0]]
        end_block = self.grid[end[1]][end[0]]

        open_list = []
        closed_list = []

        open_list.append(start_block)

        while len(open_list) > 0:
            current_block = open_list[0]

            for i in range(1, len(open_list)):
                if open_list[i].f_cost() < current_block.f_cost() or open_list[i].f_cost() == current_block.f_cost() and open_list[i].hCost < current_block.hCost:
                    current_block = open_list[i]

            open_list.remove(current_block)
            closed_list.append(current_block)
            current_block.set_closed()

            draw()

            if current_block == end_block:
                self.retrace_path(start_block, end_block)
                return

            for neighbour in self.grid_object.get_neighbours(current_block):
                if neighbour.type == b.BlockType.WALL or neighbour in closed_list:
                    continue

                new_cost_to_neighbour = current_block.gCost + self.get_distance(current_block, neighbour)

                if new_cost_to_neighbour < neighbour.gCost or neighbour not in open_list:
                    neighbour.gCost = new_cost_to_neighbour
                    neighbour.hCost = self.get_distance(neighbour, end_block)
                    neighbour.parent = current_block

                    if neighbour not in open_list:
                        open_list.append(neighbour)
                        neighbour.set_open()

