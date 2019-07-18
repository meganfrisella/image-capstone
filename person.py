class person:
    '''Person object for facial recognition
    
    Parameters:
    ----------
    name [string]
        Full name of the person 
    descriptor [array of shape (128,)]
        initial 128-d descriptor vector
        
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
    def __init__(self,name,descriptor):
        self.name = name
        self.descriptors = [descriptor]
    
    def mean_descriptor(self):
        """
        returns 128-d NumPy vector for the average descriptor of the person
        
        Parameters:
        -----------
        None
        
        Returns:
        --------
        [array shape (128,)]
            Average descriptor for the person"""
        return np.mean(self.descriptors,axis =0)
    
    def add_descriptor(self,descriptor):
        """
                Adds a 128-d descriptor to the person's descriptor list
    
        Parameters:
        ----------
        descriptor [array shape (128,)]
        
        Returns:
        --------
        None"""
        
        self.descriptors.append(descriptor)