from node import *

# general search algorithm
def general_search(problem, strategy):

    open_list = []

    open_list.append(root_node)

    while True:
        if not child_nodes:
            return 0

        if goalCheck(current_node) == True:
            return solution

        else:
            for child in child_nodes:
                if child not in open_list:
                    open_list.append(child)
                elif child in open_list:
                    index = open_list.index(child)
                    if (child.calcCost() < open_list[index].calcCost()):
                        open_list[index] = child

# successor function
def succ(current_node, operator):



    return state


