import numpy as np
import random

#initialize this to all the descriptor vectors
#Change this:
cutoff = 0.2

class Node:
    def __init__(self, ID, label, neighbors, image_path):
        self.id = ID
        self.label = label
        self.neighbors = neighbors
        self.image_path = image_path

def weight(v1, v2, cutoff):
    """
    parameters: np.array(float) shape: (128,), np.array(float) shape: (128,), float
    returns: boolean
    This function takes two 128-dimensional vectors and returns whether this person is a match for the vector
    """

    temp = v1 - v2
    temp = temp ** 2
    if np.sum(temp) ** 1 / 2 < cutoff:
        return 1 / np.sum(temp)
    return 0

def create_graph_and_matrix(descriptors):
    """
    :param descriptors: list() of np.array
    :return: list() of nodes, numpy.array
    Turns descriptors into a graph and an adjacency matrix
    """
    graph = list()
    adjacency_matrix = np.zeros((descriptors.shape[0], descriptors.shape[0]))
    for i, j in enumerate(descriptors):
        neighbors = list()
        for k, l in enumerate(descriptors):
            if j == l:
                continue
            weight = weight(j, l, cutoff)
            adjacency_matrix[i][k] = weight
            adjacency_matrix[k][i] = weight
            if adjacency_matrix[i][k] != 0:
                neighbors.append(k)

        graph.append(Node(i, i, neighbors))
    return graph, adjacency_matrix

def create_clusters(graph, adjacency_matrix):
    """
    :param graph: list() of nodes
    :param adjacency_matrix: numpy.array
    :return: dict()
    This function turns a graph of nodes into a list of images that correspond to a cluster
        """
    decrease = 0
    while decrease < graph.shape[0]*1.5:
        index = random.randint(0, graph.shape[0])
        node = graph[index]
        weight_pairings = dict()
        for i in node.neighbors:
            neighbor = graph[i]
            if neighbor.label in weight_pairings:
                weight_pairings[neighbor.label] += adjacency_matrix[index][i]
            else:
                weight_pairings[neighbor.label] = adjacency_matrix[index][i]

        inverse = [(value, key) for key, value in weight_pairings.items()]

        if node.id != max(inverse)[1]:
            decrease = 0
            node.id = max(inverse)[1]
        decrease += 1

    clusters = dict()
    for node in graph:
        if node.label in clusters:
            clusters[node.label].append(node.image_path)
        else:
            clusters[node.label] = [node.image_path]
    return clusters