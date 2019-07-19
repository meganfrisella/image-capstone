import ConvertToDescriptor as convert
import Whispers

images = ["c1.jgp", "c2.jpeg", "m1.jpeg", "m2.jpeg", "v1.JPG", "v2.JPG"]
descriptors = list()
file_paths = list()
cutoff = 0.12

for image in images:
    ds = convert.jpeg_to_descriptors("c1.jpg")
    descriptors.extend(ds)
    file_paths.extend([image for i in range(ds)])

clusters = Whispers.create_clusters(Whispers.create_graph_and_matrix(descriptors, file_paths, cutoff))
