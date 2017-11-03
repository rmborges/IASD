from general_search import *
from uninformed import *
from read_data import *
from structs import *
import sys

# leitura das opções da linha de comandos

if sys.argv[1] == '-i':
    informed = 1  # informed search

if sys.argv[1] == '-u':
    informed = 0  # uninformed search

# ficheiro com os dados do problema
file = sys.argv[2]

# leitura dos dados do ficheiro
lists = read_data(file)

# listas de vértices e launches
[vertex_list, launch_list] = lists

# root node (nada no espaço)
root_node = Node()

# classe que constrói o problema
solve = GeneralSearch(root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list, informed)

# algoritmo de procura (general search)
solution = solve.solver()

# impressão da solução
if solution:
    printSolution(solution, launch_list)
else:
    print(0)  # se não existe solução
