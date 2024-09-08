class Node:
    def __init__(self, label):
        self.label = label

    def getLabel(self):
        return self.label
    
    def __str__(self):
        return self.label

class Graph:
    def __init__(self):
        self.nodes = []     # list of nodes
        self.edges = {}     # adjacency list 

    def addNode(self, node):
        if node in self.edges:
            print("error: trying to add existing node")
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, first_node, second_node, weight):
        first = self.getNode(first_node)
        second = self.getNode(second_node)

        if not (first in self.edges and second in self.edges):
            print("error: given nodes of an edge don't exist in the graph")
            return

        self.edges[first].append((second, weight))
        self.edges[second].append((first, weight))

    def neighboursOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, label):
        for n in self.edges:
            if n.getLabel() == label:
                return n
        print("error: there's no node with the given label")
        return None

    def __str__(self):
        result = ''
        for first in self.edges:
            for second, weight in self.edges[first]:
                result = result + first.getLabel() + ' --- ' + str(weight) + ' --- ' + second.getLabel() + '\n'

        return result[:-1] # omit final newline


if __name__ == "__main__":
    graph = Graph()

    node_labels = {}

    with open("nodes", "r") as f:
        for line in f.readlines():
            tokens = line.split(' ')
            id, label = int(tokens[0]), tokens[1].strip()
            node_labels[id] = label
            graph.addNode(Node(label))
            
    with open("edges", "r") as f:
        for line in f.readlines():
            tokens = line.split(' ')
            first, second, weight = int(tokens[0]), int(tokens[1]), int(tokens[2])  

            first_label = node_labels[first]
            second_label = node_labels[second]

            graph.addEdge(first_label, second_label, weight)
    
    print(graph)
        