from structs import *
import copy

# funções dependentes do problema


def successorFunc(current_node, vertex_list, launch_list, gfunc):
    node_list = []

    if current_node.level == len(launch_list):
        return node_list

    launch = launch_list[current_node.level]

    parent_weight = current_node.total_weight()
    n = 0
    empty_node = Node()
    empty_node.parent = current_node
    empty_node.level = current_node.level + 1
    empty_node.in_space=current_node.in_space
    empty_node.num_vertex = 0
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
                        if ((vertex.connected_to_list(node.in_space)) or (not current_node.in_space)):
                            new_node = Node()
                            new_node.copy_node(node)
                            new_node.num_vertex = n
                            new_node.parent = current_node
                            new_node.in_space.append(vertex)
                            new_node.level = current_node.level + 1
                            node_weight = new_node.total_weight() - parent_weight
                            #new_node.tot_cost = gfunc(node_weight, launch)
                            new_node.tot_cost = new_node.parent.tot_cost + gfunc(node_weight, launch)
                            if not check_repeated(new_node, node_list):
                                if not exceed_payload(node_weight, launch.max_payload):
                                    node_list.append(new_node)
                                    test = 1

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

def gFunc(node_weight, launch): #ver launch level
    cost = launch.fixed_cost + node_weight*launch.variable_cost
    return cost

def printSolution(node, launch_list):
    sum_costs = 0
    cleanPreviousVertex(node)
    while node and node.level > 0:
        level = node.level
        id_list = []
        for vertex in node.in_space:
            id_list.append(vertex.id)
        if id_list:
            print(launch_list[level-1].date, id_list, node.tot_cost)
        sum_costs = sum_costs + node.tot_cost
        node = node.parent
    print(sum_costs)

def cleanPreviousVertex(node):
    father = node.parent
    while father:
        l = len(node.in_space)
        i = 0
        index = 0
        while i < l:
            if node.in_space[index].search_in_list(father.in_space):
                del node.in_space[index]
            else:
                index = index + 1
            i = i + 1


        node = father
        father = father.parent
