from uninformed from *

# general search algorithm
class GeneralSearch:

    def __init__(self, root_node, strategyFunc, goalCheck, successorFunc, gFunc):
        self.root_node = root_node
        self.strategyFunc = strategyFunc
        self.goalCheck = goalCheck
        self.successorFunc = successorFunc
        self.gFunc = gFunc
        self.open_list = []

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
            if goalCheck(node) == True:
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