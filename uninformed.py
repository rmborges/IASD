from structs import *
# funções dependentes do problema


def successorFunc(node, vertex_list, launch_list):
    i=0
    for vertex in vertex_list[:]:
        if not(vertex.search_in_list(node.in_space)):
            i=i+1







def strategyFunc(open_list):
    return min(open_list, key=lambda node: node.cost)

def goalCheck():


def gFunc(node):





    return cost