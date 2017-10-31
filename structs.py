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
            if vertex.id == self.id:
                return 1
        return 0

    def connected_to_list(self, vertex_list):
        for vt in vertex_list:
            if self.search_in_list(vt.connect):
                return 1
        return 0


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

    def __init__(self, date,date_ord, max_payload, fixed_cost, variable_cost, level):
        self.date = date
        self.date_ord = date_ord
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
        self.level = level


    def print_launch(self):
        print('launch', self.date, self.max_payload, self.fixed_cost, self.variable_cost, self.level)


class Node(object):

    def __init__(self):
        self.parent = []
        self.in_space = []
        self.added=[]
        self.tot_cost = 0
        self.num_vertex = 0
        self.level = 0
        self.heuristic = 0

    def print_node(self):
        print('node:')
        print('num vertex added:',self.num_vertex)
        for vertex in self.in_space:
            print('in_space', vertex.id)
        print('total cost up to node:',self.tot_cost)
        print('\n')

    def copy_node(self,old_node):
        self.num_vertex=old_node.num_vertex
        self.level=old_node.level
        for vertex in old_node.in_space:
            self.in_space.append(vertex)
        for vertex in old_node.added:
            self.added.append(vertex)
        self.tot_cost=old_node.tot_cost

    def total_weight(self):
        total_weight = 0
        for vertex in self.in_space:
            total_weight = total_weight + vertex.weight
        return total_weight

    def __lt__(self, other):
        if (self.tot_cost+self.heuristic)<=(other.tot_cost+other.heuristic):
            return True
        return False