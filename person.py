import numpy as np

class Person:
    '''Person object for facial recognition
    
    Parameters:
    ----------
    name [string]
        Full name of the person 
    descriptor_input [128-d vector or tuple of array of shape (128,)]
        initial descriptor vector or tuple of 128-d descriptor vectors
        
    Variables:
    ----------
    name [string]
        Full name of the person
    descriptors [list]
        Tuple of all descriptors associated with the person
    
    Functions:
    ----------
    
    mean_descriptor()
        returns 128-d NumPy vector for the average descriptor of the person
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        [array shape (128,)]
            Average descriptor for the person
        
    add_descriptor(descriptor)
        Adds a 128-d descriptor to the person's descriptor list
    
        Parameters:
        ----------
        descriptor [array shape (128,)]
        
        Returns:
        --------
        None
    
    '''
    def __init__(self,name,descriptor_input):
        self.name = name
        if isinstance(descriptor_input,tuple):
            self.descriptors = [i for i in descriptor_input]
        if isinstance(descriptor_input,np.ndarray):
            self.descriptors = descriptor_input
        self.mean_descriptor = np.mean(self.descriptors,axis=0)

        
    def __repr__(self):
        return "P: {} ∆ {}".format(self.name,len(self.descriptors))
    
    
    def add_descriptor(self,descriptor,database):
        """
                Adds a 128-d descriptor to the person's descriptor list
                Also recomputes the mean_descriptor value
    
        Parameters:
        ----------
        descriptor [array shape (128,)]

        database [dict]
        
        Returns:
        --------
        None"""
        
        self.descriptors.append(descriptor)
        self.mean_descriptor = np.mean(self.descriptors,axis =0)
        f = open('database.p','wb')
        pickle.dump(database,f)
        f.close

    def match(self, v2, cutoff):
        """
        parameters: np.array(float) shape: (128,), float
        returns: boolean
        This function takes a 128-dimensional vectors and returns whether this person is a match for the vector
        """

        temp = self.mean_descriptor - v2
        temp = temp ** 2
        return np.sum(temp) ** 1 / 2 < cutoff