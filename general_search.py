from uninformed import *
from queue import PriorityQueue
import copy

# general search algorithm

class GeneralSearch:

    def __init__(self, root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list, informed):
        self.root_node = root_node
        self.strategyFunc = strategyFunc
        self.goalCheck = goalCheck
        self.successorFunc = successorFunc
        self.gFunc = gFunc
        self.vertex_list = vertex_list
        self.launch_list = launch_list
        self.informed = informed

    def solver(self):
        frontier = PriorityQueue()
        frontier.put((self.root_node.tot_cost, self.root_node))
        child_nodes = []

        i=0

        while True:

            if frontier.empty():
                #print('Failure: frontier list vazia.')
                return False

            # Retrieve the node with the lowest cost
            cost_and_node = frontier.get()
            node = cost_and_node[1]

            i=i+1

            #frontier.remove(node)

            # objetivo atingido (GOAL)?
            if self.goalCheck(node, self.vertex_list):
                print(i)
                return node # retorna solução

            # successor function
            child_nodes = successorFunc(node, self.vertex_list, self.launch_list, self.gFunc, self.informed)

            for child in child_nodes:
                #if child not in frontier:
                value = child.tot_cost + child.heuristic
                frontier.put((value, child))
                #elif child in frontier:
                #    print(AAAAAAAAAA)
                #    index = frontier.index(child)
                #    if child.tot_cost < frontier[index].tot_cost:
                #        frontier[index] = child
