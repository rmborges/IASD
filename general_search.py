from node import *

# general search algorithm
class GeneralSearch:

    def __init__(self, root_node, goal, successorFunc, strategyFunc):
        self.root_node = root_node
        self.goal = goal
        self.open_list = []
        self.successorFunc = succFunc
        self.strategyFunc = strategyFunc

    def solver(self):

        # inserir root node na open list
        self.open_list.append(root_node)

        while True:

            # open list vazia?
            if not self.open_list:
                print('Failure: open list vazia.')
                quit()

            # escolher node de acordo com strategy function
            node = self.strategyFunc(self.open_list)

            # remoção da open list - PÔR NA STRATEGY FUNC?
            self.open_list.remove(node)

            # objetivo atingido (GOAL)?
            if (node.testGoal(self.goal)):
                return node # retorna solução

            #
            child_nodes = node.getChildNodes()

            for child in child_nodes:
                if child not in self.open_list:
                    self.open_list.append(child)
                elif child in self.open_list:
                    index = self.open_list.index(child)
                    if child.cost < self.open_list[index].cost:
                        self.open_list[index] = child



def successorFunc():


def strategyFunc():
