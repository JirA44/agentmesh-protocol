# This is the state machine for the bounty system
# The state machine tracks the current state of the bounty and the number of bounties available
# The goal is to find the minimum number of bounties needed to reach a certain state
# The solution uses a breadth-first search (BFS) approach to explore all possible paths and find the shortest path to the desired state

import collections

def find_bounty_state():
    # Create a queue for BFS
    queue = collections.deque()
    # Initialize the starting state
    state = {"current": "active", "bounties": 0}
    queue.append(state)
    visited = set()
    visited.add(state)
    
    # Define the transitions between states
    transitions = {
        "active": {
            "active": {"bounties": 1, "current": "active"},
            "active": {"bounties": 2, "current": "active"},
            "active": {"bounties": 3, "current": "active"},
            "active": {"bounties": 4, "current": "active"},
            "active": {"bounties": 5, "current": "active"},
            "active": {"bounties": 6, "current": "active"},
            "active": {"bounties": 7, "current": "active"},
            "active": {"bounties": 8, "