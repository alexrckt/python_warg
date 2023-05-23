import random

from algo_pathfinding.astar import *


def grid_generator(M, N):
    grid = []
    for row_num in range(0, M):
        row = []
        for column_num in range(0, N):
            tile = 1 if random.randrange(0, 100) < 30 else 0
            row.append(tile)
        grid.append(row)
    return grid


def validate_coords(grid, i, j):
    return True if grid[i][j] == 0 else False


def main():
    M, N = map(int, input('Enter grid height and width separated by space: ').split())
    grid = grid_generator(M, N)
    while True:
        start_coord = [int(num) for num in input('Enter start point coordinates separated by space: ').split()]
        if validate_coords(grid, start_coord[0], start_coord[1]) is not True:
            print('Coordinates are occupied by earth, please enter other coordinates')
            continue

        end_coord = [int(num) for num in input('Enter end point coordinates separated by space: ').split()]
        if validate_coords(grid, end_coord[0], end_coord[1]) is not True:
            print('Coordinates are occupied by earth, please enter other coordinates')
            continue
        break

    start_node = Node(start_coord[0], start_coord[1])
    end_node = Node(end_coord[0], end_coord[1])

    path = astar(grid, start_node, end_node)
    print(path)


if __name__ == "__main__":
    main()