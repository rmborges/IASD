#classes que armazenam os dados

class Vertex(object):

    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.connect = []

    def print_vertex(self):
        print('\nvertex', self.id, self.weight)
        for vertex in self.connect[:]:
            print(vertex.id)

    def add_connect(self, connect):
        self.connect.append(connect)

    def search_in_list(self, vertex_list):
        for vertex in vertex_list[:]:
            if(vertex.id == self.id):
                return 1;
        return 0;



class Edge(object):

    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def print_edge(self):
        print('edge', self.vertex1.id, self.vertex1.weight, self.vertex2.id, self.vertex2.weight)

    def add_weight(self, vertex_list):
        for vertex in vertex_list[:]:
            if(self.vertex1.id == vertex.id):
                self.vertex1.weight = vertex.weight
            if(self.vertex2.id == vertex.id):
                self.vertex2.weight = vertex.weight



class Launch(object):

    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost

    def print_launch(self):
        print('launch', self.date, self.max_payload, self.fixed_cost, self.variable_cost)


class Node(object):



    def __init__(self):
        self.parent = []
        self.children = []
        self.in_space = []
        self.tot_cost = 0
        self.vertex_to_add = []
        self.level = 0