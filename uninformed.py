from structs import *
from read_data import *
from general_search import *
# funções dependentes do problema


def successorFunc(in_space):

    teste = 1
    while teste == 1:
        teste = 0


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