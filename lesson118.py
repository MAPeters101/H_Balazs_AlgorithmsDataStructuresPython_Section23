import heapq
from turtledemo.forest import start


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


class DijkstraAlgorithm:

    def __init__(self):
        # this is the heap representation (binary heap and not Fibonacci heap)
        self.heap = []

    def calculate(self, start_vertex):

        # initialize the vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        # have to iterate until the heap is not empty
        while self.heap:

            # we pop the vertex with lowest min_distance parameter
            # pop function removes the given item !!!
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # we have to consider the neighbors
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                # we have to compare the min_distances
                new_distance = u.min_distance + edge.weight

                # there is a shorter path to the v vertex
                if new_distance < v.min_distance:
                    # when there is a shortest path available then we update the
                    # predecessor accordingly
                    v.predecessor = u
                    v.min_distance = new_distance
                    # update the heap - this is the lazy implementation
                    # WHY? Because it takes O(N) to find the vertex we want to update (v)
                    # plus we have O(logN) to handle the heap again [O(N)+O(logN)=O(N)]
                    # Fibonacci heaps - O(1)
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

        @staticmethod
        def get_shortest_path(vertex):

            print("Shortest path to vertex is: %s" % str(vertex.min_distance))

            actual_vertex = vertex

            while actual_vertex.predecessor is not None:
                print("%s " % actual_vertex.name)
                actual_vertex = actual_vertex.predessor




