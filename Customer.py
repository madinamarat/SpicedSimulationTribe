
class Customer: 
    '''
    Customer for supermarket simulation.
    
    Parameters :
    ------------
    trans_prob_matrix - as pandas DataFrame with current location as columns headers and next possible location as index.
    finished - Default : False ; will be set to True once customer reaches checkout -> allows if-conditionally for deactivation.
    location - Default : 'entrance'
    
    '''
    
    def __init__(self, trans_prob_matrix: pandas.core.frame.DataFrame, finished=False, location='entrance'):
        self.trans_prob_matrix
        self.finished = finished
        self.location = location
        
    def change_location(self):
        '''
        Method of the Customer class to change the current_location.
        
        ### ==> Needs to be called, which could be done by storing each created customer object in a list.
        '''
        if location != 'checkout' and finished == False:
            self.location = np.random.choice(list(trans_prob_matrix.index), p=list(trans_prob_matrix[location]))
            
            # return self.location or 'return location?' 
            # - do we need this, or will other functions just make use of customers location to display object appropiately?
        
        else:
            self.finished = True
