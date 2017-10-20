from structs import *
from read_data import *
# funções dependentes do problema


def successorFunc(in_space, launch_list):

    linked = []

    for vertex in in_space[:]:
        for connect in vertex.connect[:]:
            if not connect in in_space:
                linked.append(connect)
    return linked


def strategyFunc(open_list):
    return min(open_list, key=lambda node: node.cost)

def goalCheck():
    for vertex in vertex_list:
        if not vertex in node.in_space:
            return False
    return True

def gFunc(vertex_no, launch):
    cost = launch.fixed_cost + vertex_no*launch.variable_cost
    return cost