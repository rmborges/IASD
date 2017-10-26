from uninformed import *
import copy

# general search algorithm

class GeneralSearch:

    def __init__(self, root_node, strategyFunc, goalCheck, successorFunc, gFunc, vertex_list, launch_list):
        self.root_node = root_node
        self.strategyFunc = strategyFunc
        self.goalCheck = goalCheck
        self.successorFunc = successorFunc
        self.gFunc = gFunc
        self.vertex_list = vertex_list
        self.launch_list = launch_list



    def solver(self):
        frontier = [self.root_node]  # priority queue
        explored = []  # priority queu
        child_nodes = []

        while True:

            if not frontier:
                print('Failure: frontier list vazia.')
                return False

            # Retrieve the node with the lowest cost
            node = min(frontier, key=lambda node: node.tot_cost)
            #node = frontier.pop()
            frontier.remove(node)

            # objetivo atingido (GOAL)?
            if self.goalCheck(node, self.vertex_list):
                return node # retorna solução

            #explored.append(node)

            # successor function
            child_nodes = successorFunc(node, self.vertex_list, self.launch_list, self.gFunc)
            #children = successorFunc(node, self.vertex_list, self.launch_list, self.gFunc)
            #child_nodes = copy.deepcopy(children)

            for child in child_nodes:
                #child.print_node()
                if child not in (frontier or explored):
                    frontier.append(child)
                #elif child in frontier:
                #    index = frontier.index(child)
                #    if child.tot_cost < frontier[index].tot_cost:
                #        frontier[index] = child
