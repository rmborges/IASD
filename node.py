# classe Node

class Node(object):


    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.vertex_list = []
        self.tot_cost = 0
        self.level = 0


