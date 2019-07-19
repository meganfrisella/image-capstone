import ConvertToDescriptor as convert
import numpy as np
import Whispers
import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io
images = ["\c1.jpg", "\c2.jpeg", "\m1.jpeg", "\m2.jpeg", r"\v1.JPG", r"\v2.JPG"]
myPath = r"C:\Users\Vaishnavi\Desktop\CogWorks\CapstoneProjects\image-capstone\images"
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
my_path = r"C:\Users\Vaishnavi\Desktop\CogWorks\CapstoneProjects\image-capstone\images\\"

try:
    from jupyterthemes import jtplot

    jtplot.style()
except ImportError:
    pass


def display_clusters(database):
    num_people = len(database)
    max_num_images = 0

    for name in database.keys():
        if (len(database[name]) > max_num_images):
            max_num_images = len(database[name])

    for y, name in enumerate(database.keys()):
        img_names = database[name]

        for i in range(max_num_images):
            plt_idx = i * num_people + y + 1
            plt.subplot(max_num_images, len(database), plt_idx)

            if i < len(img_names):
                plt.imshow(io.imread(my_path + img_names[i]))
            else:
                plt.imshow(io.imread(my_path + "blank.png"))

            plt.axis('off')
            if i == 0:
                plt.title(("Person "+str(y)))

    plt.show()
display_clusters(clusters)