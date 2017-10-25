from general_search import *
from uninformed import *
from read_data import *
from structs import *


lists = read_data()

[vertex_list, launch_list] = lists

root_node = Node() # empty node (nothing in space)

solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list)

solution = solve.solver()

if solution:
    printSolution(solution, launch_list)
else:
    print('\n::: No solution!\n')


