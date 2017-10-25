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
        self.open_list = []
        self.vertex_list = vertex_list
        self.launch_list = launch_list

    def solver(self):
        child_nodes = []

        # inserir root node na open list
        self.open_list.append(self.root_node)

        while True:

            # open list vazia?
            if not self.open_list:
                print('Failure: open list vazia.')
                return False

            # escolher node de acordo com strategy function
            curr_node = self.strategyFunc(self.open_list)
            node = copy.deepcopy(curr_node)

            # remoção da open list
            self.open_list.remove(curr_node)

            # objetivo atingido (GOAL)?
            if self.goalCheck(node, self.vertex_list):
                return node # retorna solução

            # successor function
            children = successorFunc(node, self.vertex_list, self.launch_list, self.gFunc)
            child_nodes = copy.deepcopy(children)

            for child in child_nodes:
                #child.print_node()
                if child not in self.open_list:
                    self.open_list.append(child)
                    print(1)
                #elif child in self.open_list:
                #    index = self.open_list.index(child)
                #    if child.tot_cost < self.open_list[index].tot_cost:
                #        self.open_list[index] = child
