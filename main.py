from general_search import *
from uninformed import *
from read_data import *
from structs import *
from time import *
import sys

# default option for data file
file = 'iss.txt'

# parse command line arguments

# uninformed or informed method
#if sys.argv[1][1] == '-i':
    #informed = 1
#if sys.argv[1][1] == '-u':
    #informed = 0

# file with data
#file = sys.argv[2]

# read data from file
lists = read_data(file)

[vertex_list, launch_list] = lists

# root node - empty node (nothing in space)
root_node = Node()

# in/uninformed
informed = 1

solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list, informed)

initial_time = time()

solution = solve.solver()

total_time = time() - initial_time

if solution:
    printSolution(solution, launch_list)
else:
    print(0)

print('\nElapsed time: ', total_time, 's')


