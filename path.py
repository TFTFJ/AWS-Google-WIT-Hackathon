class graph:
    def __init__(self):
        dictionary = {}
        vertices = []
        self.dictionary = dictionary
        self.vertices = vertices

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.dictionary[vertex] = []
            self.vertices.append(vertex)

    def add_edge(self, src_vertex, dest_vertex, weight):
        outgoing_edge = (dest_vertex, weight)
        self.dictionary[src_vertex].append(outgoing_edge)

    def get_vertices(self):
        return self.vertices
        
    def get_weight(self, src, dest):
        for edge in self.dictionary[src]:
            if edge[0] == dest:
                return edge[1]

    def neighbour(self, vertex):
        result = []
        for edge in self.dictionary[vertex]:
            if edge not in result:
                result.append(edge[0])
        return result

class water_source:
    def __init__(self):
        sources = []
        self.sources = sources

def dijkstra(gph, src_vertex):
    unvisited = gph.get_vertices()
    dist = {}
    pred = {}
    for vertex in unvisited:
        dist[vertex] = float('inf')
    dist[src_vertex] = 0
    while unvisited:
        current_min = None
        for vertex in unvisited: # Iterate over the nodes
            if current_min == None:
                current_min = vertex
            elif dist[vertex] < dist[current_min]:
                current_min = vertex
        neighbors = gph.neighbour(current_min)
        for neighbor in neighbors:
            weight = dist[current_min] + gph.get_weight(current_min, neighbor)
            if weight < dist[neighbor]:
                dist[neighbor] = weight
                pred[neighbor] = current_min
        unvisited.remove(current_min)
    
    return pred, dist

g = graph()
g.add_vertex("s")
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")

g.add_edge("s", "a", 10)
g.add_edge("s", "c", 5)

g.add_edge("a", "b", 1)
g.add_edge("a", "c", 2)

g.add_edge("b", "d", 4)

g.add_edge("c", "a", 3)
g.add_edge("c", "b", 9)
g.add_edge("c", "d", 2)

g.add_edge("d", "s", 7)
g.add_edge("d", "b", 6)

pred, dist = dijkstra(g, "s")
print(dist)
for key in sorted(pred):
    print("%s: %s" % (key, pred[key]))