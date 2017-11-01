from structs import *
import copy

# funções dependentes do problema


def successorFunc(current_node, vertex_list, launch_list, gFunc, informed):
    node_list = []

    if current_node.level == len(launch_list):
        return node_list



    parent_weight = current_node.total_weight()

    #Criar node vazio que serve de base aos restantes mas que no fim será removido
    empty_node = Node()
    empty_node.parent = current_node
    empty_node.level = current_node.level
    empty_node.in_space=current_node.in_space
    empty_node.num_vertex = 0
    empty_node.tot_cost=current_node.tot_cost
    node_list.append(empty_node)

    level = current_node.level
    #Ciclo para criar nodes
    while level < len(launch_list):
        launch = launch_list[level]
        level=level+1
        node_list[0].level=level
        n=0
        test=1
        while test:
            test = 0
            n = n + 1
            for node in node_list:
                if (node.num_vertex == (n-1)) and (node.level == level):
                    for vertex in vertex_list:
                        if (not vertex.search_in_list(node.in_space)) and (vertex.connected_to_list(node.in_space)) :
                            new_node = Node()
                            new_node.copy_node(node)
                            new_node.num_vertex = n
                            new_node.parent = current_node
                            new_node.in_space.append(vertex)
                            new_node.added.append(vertex)
                            new_node.level = level
                            new_node.tot_cost = new_node.tot_cost + gFunc(n, vertex, launch)
                            node_weight = new_node.total_weight()-parent_weight
                            if not check_repeated(new_node, node_list) and (not exceed_payload(node_weight, launch.max_payload)):
                                node_list.append(new_node)
                                test = 1

    node_list.remove(node_list[0])

    # elimina casos em que o peso restante excede o dos lançamentos que faltam
    if node_list:
        i=0
        while(i<len(node_list)):
            node=node_list[i]
            remaining_weight = 0
            for vertex in vertex_list:
                if vertex not in node.in_space:
                    remaining_weight = remaining_weight + vertex.weight

            if remaining_weight > (launch_list[node.level-1].rem_weight-launch_list[node.level-1].max_payload):
                node_list.remove(node)
                # heuristic value
            else:
                i=i+1
                if informed:
                    node.heuristic = launch_list[node.level-1].min_vc * remaining_weight
                if not informed:
                    node.heuristic = 0


    return node_list


def check_repeated(node, node_list):
    for nd in node_list:
        if ((nd.num_vertex == node.num_vertex) and (node.level == nd.level)):
            i = 0
            for vertex in node.in_space:
                if vertex.search_in_list(nd.in_space):
                    i=i+1
            if i == len(nd.in_space):
                return 1
    return 0

def exceed_payload(node_weight, max_payload):
    if (node_weight > max_payload):
        return 1
    return 0


def strategyFunc(open_list):
    return min(open_list, key=lambda node: node.tot_cost)

def goalCheck(node, vertex_list):
    for vertex in vertex_list:
        if not vertex.search_in_list(node.in_space):
            return False
    return True

def gFunc(n, vertex, launch): #ver launch level
    cost = 0
    if n == 1:
        cost = launch.fixed_cost
    cost = cost + vertex.weight*launch.variable_cost
    return cost

def printSolution(node, launch_list):
    #sum_costs = 0
    mission_cost=node.tot_cost
    #cleanPreviousVertex(node)
    level=node.level

    while level>0:
        id_list = []
        for vertex in node.added:
            id_list.append(vertex.id)
        if id_list:
            vertex_string = ''
            for id in id_list:
                vertex_string = vertex_string + ' ' + id
            print(launch_list[level-1].date, vertex_string, node.tot_cost-node.parent.tot_cost)
        level=node.parent.level
        node=node.parent
    print(mission_cost)