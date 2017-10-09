class Vertex(object):
    id = ""
    weight = 0
    connect = []

    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def print_vertex(self):
        print('vertex', self.id, self.weight)
        for vertex in self.connect[:]:
            print(vertex.id)

    def add_connect(self, connect):
        self.connect.append(connect)

class Edge(object):
    vertex1 = ""
    vertex2 = ""

    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def print_edge(self):
        print('edge', self.vertex1, self.vertex2)

class Launch(object):
    date= ""
    max_payload = 0
    fixed_cost = 0
    variable_cost = 0

    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost

    def print_launch(self):
        print('launch', self.date, self.max_payload, self.fixed_cost, self.variable_cost)

# leitura do ficheiro com os dados
iss_data = open('iss.txt', 'r')

v = 0
vertex_list = []

e = 0
edge_list = []

l = 0
launch_list = []



while True:
    line = iss_data.readline()

    if not line:
        break

    fields = line.split()

    if line[0] == 'V':
        id = fields[0]
        weight = float(fields[1])
        vertex_list.append(Vertex(id, weight))
        v = v + 1

    if line[0] == 'E':
        vertex1 = fields[1]
        vertex2 = fields[2]
        edge_list.append(Edge(vertex1, vertex2))
        edge_list[e].print_edge()
        e = e + 1

    if line[0] == 'L':
        date = fields[1]
        max_payload = fields[2]
        fixed_cost = fields[3]
        variable_cost = fields[4]

        launch_list.append(Launch(date, max_payload, fixed_cost, variable_cost))
        launch_list[l].print_launch()
        l = l + 1


for edge in edge_list[:]:
    vertex1=edge.vertex1
    vertex2=edge.vertex2

    for vertex in vertex_list[:]:
        if vertex.id == vertex1:
            vertex.add_connect(vertex)
        if vertex.id == vertex2:
            vertex.add_connect(vertex)

for vertex in vertex_list[:]:
    vertex.print_vertex()