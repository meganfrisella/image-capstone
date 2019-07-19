import ConvertToDescriptor as convert
import Whispers

images = ["images/c1.jgp", "images/c2.jpeg", "images/m1.jpeg", "images/m2.jpeg", "images/v1.JPG", "images/v2.JPG"]
descriptors = list()
file_paths = list()
cutoff = 0.12

for image in images:
    ds = convert.jpeg_to_descriptors(image)
    descriptors.extend(ds)
    file_paths.extend([image for i in range(ds)])

clusters = Whispers.create_clusters(Whispers.create_graph_and_matrix(descriptors, file_paths, cutoff))
