from uninformed import *

teste = 1

n = 0

node_list = []

parent =

while teste == 1:
    teste = 0

    if n ==0:
        node_list.append(new Node())

    else:
        for node in node_list:
            if node.n == n-1:
                for vertex in vertex_list:
                    if (((vertex in vertex.connect) or (vertex in node.children)) and ((vertex not in node.children) or (vertex not in node.in_space)))
                        new_node = new Node()
                        new_node.parent = parent
                        new_node.in_space =
                        node_list.append(new_node)
                        node.n = n
                        teste = 1