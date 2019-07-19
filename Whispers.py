import numpy as np
import random

class Node:
    def __init__(self, id, label, neighbors, image_path):
        self.id = id
        self.label = label
        self.neighbors = neighbors
        self.image_path = image_path


def weight(v1, v2, cutoff):
    """
    parameters: np.array(float) shape: (128,), np.array(float) shape: (128,), float
    returns: boolean
    This function takes two 128-dimensional vectors and returns whether this person is a match for the vector
    """

    """dists = -2 * np.matmul(v1, v2.T)
    dists += np.sum(v1 ** 2, axis=1)[:, np.newaxis]
    dists += np.sum(v2 ** 2, axis=1)
    return np.sqrt(dists)"""

    temp = v1 - v2
    temp = temp ** 2
    if np.sum(temp) ** 1 / 2 < cutoff:
        return 1 / np.sum(temp)
    return 0


def create_graph_and_matrix(descriptors, image_paths, cutoff):
    """
    :param descriptors: list() of np.array
            cutoff: float
            image_paths: list of image paths corresponding to descriptors
    :return: list() of nodes, numpy.array
    Turns descriptors into a graph and an adjacency matrix
    """
    graph = list()
    adjacency_matrix = np.zeros((len(descriptors), len(descriptors)))
    for i, j in enumerate(descriptors):
        neighbors = list()
        for k, l in enumerate(descriptors):
            if i == k:
                continue
            w = weight(j, l, cutoff)
            adjacency_matrix[i][k] = w
            adjacency_matrix[k][i] = w
            if adjacency_matrix[i][k] != 0:
                neighbors.append(k)

        graph.append(Node(i, i, neighbors, image_paths[i]))
    return graph, adjacency_matrix


def create_clusters(graph, adjacency_matrix):
    """
    :param graph: list() of nodes
    :param adjacency_matrix: numpy.array
    :return: dict()
    This function turns a graph of nodes into a list of images that correspond to a cluster
        """
    #print(len(graph), graph)
    #print(adjacency_matrix)

    decrease = 0
    while decrease < len(graph)*1.5:
        index = random.randint(0, len(graph)-1)
        #print("index: ", index)
        #print(len(graph))
        node = graph[index]
        weight_pairings = dict()
        for i in node.neighbors:
            neighbor = graph[i]
            if neighbor.label in weight_pairings:
                weight_pairings[neighbor.label] += adjacency_matrix[index][i]
            else:
                weight_pairings[neighbor.label] = adjacency_matrix[index][i]
        inverse = [(value, key) for key, value in weight_pairings.items()]
        if node.label != max(inverse)[1]:
            decrease = 0
            node.label = max(inverse)[1]
        decrease += 1

    clusters = dict()
    for node in graph:
        if node.label in clusters:
            clusters[node.label].append(node.image_path)
        else:
            clusters[node.label] = [node.image_path]
    return clusters
