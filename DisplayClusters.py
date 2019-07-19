import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io

try:
    from jupyterthemes import jtplot
    jtplot.style()
except ImportError:
    pass

images = {"Megan": ["m1.jpeg", "m2.jpeg", "m3.jpeg"], "Vaishnavi": ["v1.JPG", "v2.JPG", "v3.JPG", "v4.JPG"],
          "Christian": ["c1.jpg", "c2.jpeg"]}
my_path = r"C:\Users\cbadu\Documents\BWSI_CogWorks\Capstone_Projects\Week2_Visual\image-capstone\images\\"

def display_faces(database):
    num_people = len(database)
    max_num_images = 0
    
    for name in database.keys():
        if (len(database[name]) > max_num_images):
            max_num_images = len(database[name])
    
    for y, name in enumerate(database.keys()):
        img_names = database[name]
        
        for i in range(max_num_images):
            plt_idx = i*num_people + y + 1
            plt.subplot(len(database), max_num_images, plt_idx)
            
            if i < len(img_names):
                plt.imshow(io.imread(my_path + img_names[i]))
            else:
                plt.imshow(io.imread(my_path + "blank.png"))
            
            plt.axis('off')
            if i == 0:
                plt.title(name)
    
    plt.show()