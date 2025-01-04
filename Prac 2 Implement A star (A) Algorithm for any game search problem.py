import heapq

# Define the grid dimensions and obstacles
GRID_WIDTH = 6
GRID_HEIGHT = 5
OBSTACLES = [(1, 1), (2, 2), (3, 3), (4, 3)]

# Define the initial state and goal state
initial_state = (0, 0)
goal_state = (5, 4)

# Define possible actions (moving up, down, left, or right)
def actions(state):
    x, y = state
    possible_actions = []
    if x > 0:
        possible_actions.append(('left', (x - 1, y)))
    if x < GRID_WIDTH - 1:
        possible_actions.append(('right', (x + 1, y)))
    if y > 0:
        possible_actions.append(('up', (x, y - 1)))
    if y < GRID_HEIGHT - 1:
        possible_actions.append(('down', (x, y + 1)))
    return possible_actions

# Define the cost function (all actions have a cost of 1)
def cost_fn(state, action):
    return 1

# Define the heuristic function (Manhattan distance to the goal)
def heuristic_fn(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(initial_state, goal_state, actions, cost_fn, heuristic_fn):
    open_set = []
    closed_set = set()

    initial_node = Node(state=initial_state)
    initial_node.cost = 0
    initial_node.heuristic = heuristic_fn(initial_state, goal_state)

    heapq.heappush(open_set, initial_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            return build_path(current_node)

        closed_set.add(current_node.state)

        for action, neighbor_state in actions(current_node.state):
            if neighbor_state in closed_set:
                continue

            neighbor_cost = current_node.cost + cost_fn(current_node.state, action)
            neighbor_heuristic = heuristic_fn(neighbor_state, goal_state)

            for node in open_set:
                if node.state == neighbor_state and node.cost <= neighbor_cost:
                    break
            else:
                neighbor_node = Node(state=neighbor_state, parent=current_node, action=action, cost=neighbor_cost, heuristic=neighbor_heuristic)
                heapq.heappush(open_set, neighbor_node)

    return None

def build_path(node):
    path = []
    while node is not None:
        path.append((node.state, node.action))
        node = node.parent
    return list(reversed(path))

# Find the optimal path using A*
optimal_path = astar_search(initial_state, goal_state, actions, cost_fn, heuristic_fn)

if optimal_path:
    print("Optimal Path:")
    for state, action in optimal_path:
        print(f"State: {state}, Action: {action}")
else:
    print("No path found.")
