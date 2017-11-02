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
        frontier = [self.root_node]
        explored = []
        child_nodes = []

        i=1

        while True:

            if not frontier:
                return False

            # Retrieve the node with the lowest cost
            node = min(frontier, key=lambda node: (node.tot_cost+node.heuristic))

            i = i + 1

            frontier.remove(node)

            explored.append(node)

            # goal state?
            if self.goalCheck(node, self.vertex_list):
                print(i)
                return node # retorna solução

            # successor function
            child_nodes = successorFunc(node, self.vertex_list, self.launch_list, self.gFunc, self.informed)

            for child in child_nodes:
                if child not in (frontier or explored):
                    frontier.append(child)

                elif child in frontier:
                    index = frontier.index(child)
                    if child.tot_cost < frontier[index].tot_cost:
                        frontier[index] = child
