from structs import *

#from read_data import *
# from general_search import *
# funções dependentes do problema


def successorFunc(current_node,vertex_list,max_payload):

    parent_weight = current_node.total_weight()
    node_list = []
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
                        if vertex.connected_to_list(node.in_space):
                            new_node=Node()
                            new_node.copy_node(node)
                            new_node.num_vertex = n
                            new_node.in_space.append(vertex)
                            if not check_repeated(new_node,node_list):
                                if not exceed_payload(new_node, parent_weight, max_payload):
                                    node_list.append(new_node)
                                    test = 1


    for node in node_list:
        current_node.children.append(node)
        node.print_node()


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

def exceed_payload(node, parent_weight, max_payload):
    node_weight = parent_weight - node.total_weight()
    if node_weight > max_payload:
        return 1
    return 0


def strategyFunc(open_list):
    return min(open_list, key=lambda node: node.cost)

def goalCheck():
    for vertex in vertex_list:
        if not vertex in node.in_space:
            return False
    return True

def gFunc(vertex_no, launch): #ver launch level
    cost = launch.fixed_cost + vertex_no*launch.variable_cost
    return cost