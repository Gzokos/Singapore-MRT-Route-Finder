import random

class Vertex:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.edges = []
        self.parent = None
        self.color = 'white'
        self.distance = float("inf")

    def display(self):
        print(self.key, self.data, self.distance, end=": [ ")
        for edge in self.edges:
            print(edge.connection.key, end=" ")
        print("]")

class Edge:
    def __init__(self, vertex):
        self.connection = vertex
        self.weight = 1

class Graph:
    def add_station(self, code, name):
        if code not in self.vertices:
            vertex = self.add(code)
            if vertex:
                vertex.data = f"{name} ({code})"

    def __init__(self):
        self.vertices = {}
        self.directed = False
        self.queue = []
        self.start = None

    def init_bfs(self):
        for v in self.vertices.values():
            v.parent = None
            v.distance = float("inf")
            v.color = 'white'

    def relax(self, va, vb, w):
        if va.distance + w < vb.distance:
            vb.distance = va.distance + w
            vb.parent = va

    def dijkstra(self, start):
        self.start = start
        self.init_bfs()
        if start not in self.vertices:
            return False
        v = self.vertices[start]
        v.distance = 0
        heap = []
        heap.append((0, v))
        visited = set()
        while heap:
            heap.sort(key=lambda x: x[0])
            dist_u, u = heap.pop(0)
            if u.key in visited:
                continue
            visited.add(u.key)
            for e in u.edges:
                self.relax(u, e.connection, e.weight)
                if e.connection.key not in visited:
                    heap.append((e.connection.distance, e.connection))

    def bfs(self, start):
        self.start = start
        self.init_bfs()
        if start not in self.vertices:
            return False
        v = self.vertices[start]
        v.distance = 0
        v.color = 'grey'
        self.queue.append(v)
        while self.queue:
            v = self.queue.pop(0)
            v.color = 'black'
            for e in v.edges:
                con = e.connection
                if con.color == 'white':
                    con.color = 'gray'
                    con.distance = v.distance + 1
                    con.parent = v
                    self.queue.append(con)
        return True

    def bfs_shortest_path(self, dest):
        if dest in self.vertices:
            v = self.vertices[dest]
            if v.parent is None:
                print("No path from", v.data)
                return False
            self.print_path(v)
            print()
            return True
        else:
            return False

    def print_path(self, vertex):
        if vertex.parent is not None:
            self.print_path(vertex.parent)
        print(vertex.data, end=' -> ')

    def display(self):
        for v in self.vertices.values():
            v.display()

    def add(self, key):
        if key in self.vertices:
            return None
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def connect(self, key_a, key_b, weight=1):
        if key_a not in self.vertices or key_b not in self.vertices:
            return False, "Key not found"
        vertex_a = self.vertices[key_a]
        vertex_b = self.vertices[key_b]
        edge_ab = Edge(vertex_b)
        edge_ab.weight = weight
        vertex_a.edges.append(edge_ab)
        if not self.directed:
            edge_ba = Edge(vertex_a)
            edge_ba.weight = weight
            vertex_b.edges.append(edge_ba)
        return True, "Vertices connected"
