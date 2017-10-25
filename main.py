from general_search import *
from uninformed import *
from read_data import *
from structs import *


lists = read_data()

[vertex_list, launch_list] = lists

root_node = Node() # empty node (nothing in space)
print(1)
solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list)
print(2)
solution = solve.solver()
print(3)
if solution == False:
    print('No solution!')
