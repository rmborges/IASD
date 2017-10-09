class Vertex(object):
    id = ""
    weight = 0

    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def print_vertex(self):
        print('vertex', self.id, self.weight)

class Edge(object):
    vertex1 = ""
    vertex2 = ""

    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def print_vertex(self):
        print('edge', self.vertex1, self.vertex2)

# leitura do ficheiro com os dados
iss_data = open('iss.txt', 'r')

v = 0
vertex_list = []
while True:
    line = iss_data.readline()

    if not line:
        break

    fields = line.split()

    if line[0] == 'V':
        id = fields[0]
        weight = float(fields[1])
        vertex_list.append(Vertex(id, weight))
        vertex_list[v].print_vertex()
        v = v + 1


v = 0
vertex_list = []
while True:
    line = iss_data.readline()

    if not line:
        break

    fields = line.split()

    if line[0] == 'V':
        id = fields[0]
        weight = float(fields[1])
        vertex_list.append(Vertex(id, weight))
        vertex_list[v].print_vertex()
        v = v + 1