# classe Node

class Node(object):

    parent = []
    children = []
    acc_cost = 0

    def __init__(self, parent):
        self.parent = parent

    def calcCost(self):
