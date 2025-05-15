
class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        # this is the node where we came from in the shortest path
        self.predecessor = None
        # this is how we store the children
        self.adjacency_list = []
        # this is the minimum distance (shortest path) from the source vertex (starting vertex)
        self.min_distance = float('inf')

    # this is how Python can compare objects
    # after inserting these objects into the heap
    # heap can compare the given objects !!!
    def __lt__(self, other):
        return self.min_distance < other.min_distance

