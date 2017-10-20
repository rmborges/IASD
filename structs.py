#classes que armazenam os dados

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
