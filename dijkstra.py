import pygame
from queue import PriorityQueue

class Dijkstra:
    def __init__(self, grid, draw):
        self.grid = grid
        self.draw = draw

    def reconstruct_path(self, came_from, current):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            self.draw()

    def search(self, start, end):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = {spot: float("inf") for row in self.grid for spot in row}
        g_score[start] = 0
        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((g_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()

            self.draw()

            if current != start:
                current.make_closed()

        return False