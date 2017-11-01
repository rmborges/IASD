from structs import *   #estruturas de dados

def read_data(file):

    # leitura do ficheiro com os dados
    iss_data = open(file, 'r')

    v = 0
    vertex_list = []

    e = 0
    edge_list = []

    l = 0
    aux_list = []
    launch_list = []

    launch_level = 0

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
            #edge_list[e].print_edge()
            e = e + 1

        if line[0] == 'L':
            date = fields[1]
            max_payload = float(fields[2])
            fixed_cost = float(fields[3])
            variable_cost = float(fields[4])

            date_ord=date[4]+date[5]+date[6]+date[7]+date[2]+date[3]+date[0]+date[1]

            aux_list.append(Launch(date, date_ord, max_payload, fixed_cost, variable_cost, launch_level))
            #launch_list[l].print_launch()
            launch_level = launch_level + 1
            l = l + 1

    launch_list = sorted(aux_list, key=lambda launch: launch.date_ord)

    rem_weight_dict = dict()
    vc_dict = dict()
    for launch in launch_list:
        rem_weight_dict[launch] = launch.max_payload
        vc_dict[launch] = launch.variable_cost


    for launch in launch_list:
        i = 0
        rem_weight = 0
        min_vc = float('Inf')
        min_fc = float('Inf')
        while i < (len(launch_list) - launch_list.index(launch)):
            index = launch_list.index(launch)
            l = launch_list[index+i]
            rem_weight = rem_weight + l.max_payload
            if l.variable_cost < min_vc:
                min_vc = l.variable_cost
            if l.fixed_cost < min_fc:
                min_fc = l.fixed_cost
            i = i + 1
        launch.rem_weight = rem_weight
        launch.min_vc = min_vc
        launch.min_fc = min_fc

    for edge in edge_list[:]:
        for vertex in vertex_list[:]:
            if vertex.id == edge.vertex1.id:
                vertex.add_connect(edge.vertex2)
            if vertex.id == edge.vertex2.id:
                vertex.add_connect(edge.vertex1)

    lists = [vertex_list, launch_list]
    return lists

    # order launch list by date
    #launch_list.sort(key = lambda launch: launch.date[::-1])