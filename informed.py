from structs import *
import copy

# funções dependentes do problema


def successorFunc(current_node, vertex_list, launch_list, gfunc):
    node_list = []

    if current_node.level == len(launch_list):
        return node_list

    # soma do peso que falta enviar
    remaining_weight = 0
    for vertex in vertex_list:
        if vertex not in current_node.in_space:
            remaining_weight = remaining_weight + vertex.weight

    # peso que é possível enviar nos launches restantes
    available_weight = 0
    min_cost_possible = float('Inf')
    for launch in launch_list:
        if launch_list.index(launch) >= current_node.level:
            available_weight = available_weight + launch.max_payload
            # determines the cost of a full weight launch
            max_cost = launch.fixed_cost + launch.variable_cost*launch.max_payload
            if max_cost < min_cost_possible:
                min_cost_possible = max_cost

    # não expandir se já não é possível o que resta nos launches que faltam
    if remaining_weight > available_weight:
        return node_list

    launch = launch_list[current_node.level]

    parent_weight = current_node.total_weight()
    n = 0
    empty_node = Node()
    empty_node.parent = current_node
    empty_node.level = current_node.level + 1
    empty_node.in_space=current_node.in_space
    empty_node.num_vertex = 0
    empty_node.tot_cost=current_node.tot_cost
    node_list.append(empty_node)
    test = 1


    while test:
        test = 0
        n = n + 1
        for node in node_list:
            if node.num_vertex == (n-1):
                for vertex in vertex_list:
                    if not vertex.search_in_list(node.in_space):
                        #if ((vertex.connected_to_list(node.in_space)) or (current_node.level==0)):
                        if ((vertex.connected_to_list(node.in_space)) or (not node.in_space)):
                            new_node = Node()
                            new_node.copy_node(node)
                            new_node.num_vertex = n
                            new_node.parent = current_node
                            new_node.in_space.append(vertex)
                            new_node.added.append(vertex)
                            new_node.level = current_node.level + 1
                            #node_weight = new_node.total_weight() - parent_weight
                            #new_node.tot_cost = gfunc(node_weight, launch)
                            new_node.tot_cost = new_node.tot_cost + gFunc(n, vertex, launch)
                            node_weight = new_node.total_weight()-parent_weight
                            if not check_repeated(new_node, node_list):
                                if not exceed_payload(node_weight, launch.max_payload):
                                    node_list.append(new_node)
                                    test = 1

    # A DESENVOLVER
    # soma do peso que falta enviar nos child nodes
    #remaining_weight = 0
    #for vertex in vertex_list:
    #    if vertex not in current_node.in_space:
    #        remaining_weight = remaining_weight + vertex.weight

    return node_list


def check_repeated(node, node_list):
    for nd in node_list:
        if nd.num_vertex == node.num_vertex:
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
            print(launch_list[level-1].date, id_list, node.tot_cost-node.parent.tot_cost)
        level=level-1
        node=node.parent
    print(mission_cost)