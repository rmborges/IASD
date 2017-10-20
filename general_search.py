from node import *

# general search algorithm
class generalSearch:
    def __init__(self, root_node, goal):
        self.root_node = root_node
        self.goal = goal
        self.open_list = []

    def Solve(self):
        start_node = self.start
        self.openList = [start_node]

        while (True):
            if (not self.openList):
                print('ERROR - Open list is empty. This should not have happened.')
                quit()

            # Retrieve the node with the lowest cost
            node = min(self.openList, key=lambda state: state.cost);

            # Remove it from the open list
            self.openList.remove(node)

            if (node.testGoal(self.goal)):
                # Goal achieved
                return node

            self.closedList.append(node)
            children = node.expandState()

            for child in children:
                if child not in (self.closedList or self.openList):
                    self.openList.append(child)
                elif (child in self.openList):
                    index = self.openList.index(child)
                    if (child.cost < self.openList[index].cost):
                        self.openList[index] = child

# successor function
def succ(current_node, operator):



    return state


