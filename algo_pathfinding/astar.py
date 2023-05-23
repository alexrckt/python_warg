import heapq


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g_score = float('inf')  # Cost from start node
        self.h_score = 0  # Heuristic score
        self.parent = None  # Parent node

    def f_score(self):
        return self.g_score + self.h_score

    def __lt__(self, other):
        return self.f_score() < other.f_score()

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


# A* pathfinding algorithm
def astar(grid, start, end):
    # Define heuristic function (Manhattan distance)
    def heuristic(node):
        return abs(node.row - end.row) + abs(node.col - end.col)

    # Initialize start and end nodes
    start.g_score = 0
    start.h_score = heuristic(start)
    open_set = [start]
    closed_set = []

    while open_set:
        # Get the node with the lowest F-Score
        current_node = heapq.heappop(open_set)

        if current_node == end:
            # Reconstruct the path
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return path[::-1]  # Reverse the path

        closed_set.append(current_node)

        # Check neighboring nodes
        neighbors = get_neighbor_tiles(grid, current_node)
        for neighbor in neighbors:
            if neighbor in closed_set:
                continue

            # Calculate tentative G-Score
            tentative_g_score = current_node.g_score + 1

            if tentative_g_score < neighbor.g_score:
                neighbor.parent = current_node
                neighbor.g_score = tentative_g_score
                neighbor.h_score = heuristic(neighbor)

                # Update the priority queue
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    # No path found
    return []


def get_neighbor_tiles(grid, node):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    for delta in deltas:
        new_row = node.row + delta[0]
        new_col = node.col + delta[1]

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 1:
            neighbor = Node(new_row, new_col)
            neighbors.append(neighbor)

    return neighbors
