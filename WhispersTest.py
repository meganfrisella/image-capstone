import ConvertToDescriptor as convert
import numpy as np
import Whispers

images = ["c1.jpg", "c2.jpeg", "m1.jpeg", "m2.jpeg", r"v1.JPG", r"v2.JPG"]
myPath = r"C:\Users\Vaishnavi\Desktop\CogWorks\CapstoneProjects\image-capstone\images\\"
descriptors = list()
file_paths = list()
cutoff = 0.12

for image in images:
    ds = np.array(convert.jpeg_to_descriptors(myPath + image))
    descriptors.extend(ds)
    file_paths.extend([image for i in range(len(ds))])
#print(descriptors)

graph, adjacency_matrix = Whispers.create_graph_and_matrix(descriptors, file_paths, cutoff)
#print(adjacency_matrix)
clusters = Whispers.create_clusters(graph, adjacency_matrix)
#print(clusters)

