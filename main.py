from uninformed import *
from general_search import *

root_node = Node()

root_node.parent = []
root_node.in_space = []
root_node.children = vertex_list
root_node.level = 0

solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc)