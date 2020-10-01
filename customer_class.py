'''
Contains customer class for supermarket simulation.

    -> from customer_class import Customer
'''

import numpy as np


class Customer:
    '''
    Customer for supermarket simulation.

    Parameters :
    ------------
    trans_prob_matrix - as pandas DataFrame with current location as columns headers and next possible location as index.
    finished - Default : False ; will be set to True once customer reaches checkout -> allows if-conditionally for deactivation.
    target_location - Default : 'entrance'
    current_location - Default: entrance coordinates; coordinates of each step of movement.
    '''

    def __init__(self, trans_p_matrix, current_location, finished=False, target_location='entrance'):
        '''current location needs to be coordinates of entrance, then changed accoring to moving algorithm
        # moving to coordinates of target_location'''
        self.trans_p_matrix = trans_p_matrix
        self.current_location = current_location
        self.finished = finished
        self.target_location = target_location
        


    def next_location(self):
        '''
        Method of the Customer class to select next target_location.

        ### ==> Needs to be called, which could be done by storing each created customer object in a list.
        '''
        if self.target_location != 'checkout' and self.finished == False:
            self.target_location = np.random.choice(list(self.trans_p_matrix.index), p=list(self.trans_p_matrix[self.target_location]))

            # return self.location or 'return location?'
            # - do we need this, or will other functions just make use of customers location to display object appropiately?

        else:
            self.finished = True
            ''' => Delete coordinates to make customer disappear?
            Or just delete customer from instore list (based on finished = True),
            which defines what is displayed'''

import trans_prob_matrix

