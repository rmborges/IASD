from general_search import *
from uninformed import *
from read_data import *
from structs import *
from time import *

lists = read_data()

[vertex_list, launch_list] = lists

root_node = Node() # empty node (nothing in space)

solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list)

initial_time = time()

solution = solve.solver()

total_time = time() - initial_time

if solution:
    level=solution.level
    node=solution
    while level>0:
        print(launch_list[level-1].date)
        for vertex in node.added:
            print(vertex.id)
        level=level-1
        node=node.parent




    #printSolution(solution, launch_list)
#else:
#    print('\n::: No solution!\n')

print('\nElapsed time: ', total_time, 's')


