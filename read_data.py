from structs import *   #estruturas de dados
from uninformed import *

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
        vertex1=Vertex(fields[1],0)
        vertex2=Vertex(fields[2],0)
        edge_list.append(Edge(vertex1, vertex2))
        edge_list[e].add_weight(vertex_list)
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
    for vertex in vertex_list[:]:
        if vertex.id == edge.vertex1.id:
            vertex.add_connect(edge.vertex2)
        if vertex.id == edge.vertex2.id:
            vertex.add_connect(edge.vertex1)


for vertex in vertex_list[:]:
    vertex.print_vertex()

print('\n\n\n')


Ze=Node()
Ze.in_space.append(vertex_list[0])
Ze.in_space.append(vertex_list[1])
Ze.num_vertex=2
Ze.level=1

successorFunc(Ze,vertex_list)

