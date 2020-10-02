'''
Contains customer class for supermarket simulation.

    -> from customer_class import Customer
'''

import numpy as np
import random

size = 32
sections = {
    'drinks': {'x': (100, 230-size), 'y': (170, 470-size)},
    'dairy': {'x': (340, 460-size), 'y': (170, 470-size)},
    'spices': {'x': (570, 690-size), 'y': (170, 470-size)},
    'fruit': {'x': (800, 920-size), 'y': (170, 470-size)},
    'checkout': {'x': (150, 430-size), 'y': (640, 750-size)},
    'entrance': {'x': (800, 920-size), 'y': (640, 750-size)},
    'top': {'x': (100, 920-size), 'y': (100, 170-size)},
    'bottom': {'x': (100, 920-size), 'y': (470, 540-size)},
}


def get_semi_random_coord(section):
    '''
    Generates random x and y coordinates
    in a specific section of the supermarket
    '''
    xmin, xmax = sections[section]['x']
    ymin, ymax = sections[section]['y']
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    return (x, y)


class Customer:
    '''
    Customer for supermarket simulation.

    Parameters :
    ------------
    trans_prob_matrix - as pandas DataFrame with current location as columns headers and next possible location as index.
    finished - Default : False ; will be set to True once customer reaches checkout -> allows if-conditionally for deactivation.
    target_location - Default : 'entrance'
    current_coordinates - Default: entrance coordinates; coordinates of each step of movement.
    '''

    def __init__(self, trans_p_matrix, icon, target_location='entrance', finished=False):
        '''current location needs to be coordinates of entrance, then changed accoring to moving algorithm
        # moving to coordinates of target_location'''
        self.trans_p_matrix = trans_p_matrix
        self.finished = finished
        self.target_location = target_location
        self.target_coordinates = get_semi_random_coord(target_location)
        self.current_coordinates = get_semi_random_coord(target_location)
        self.icon = icon

    def move(self):
        target = self.target_location
        cur_x, cur_y = self.current_coordinates
        tar_x, tar_y = self.target_coordinates
        xmin, xmax = sections[target]['x']
        ymin, ymax = sections[target]['y']

        ymin_top, ymax_top = sections['top']['y']
        ymin_bottom, ymax_bottom = sections['bottom']['y']

        # within correct x coordinates
        if xmin < cur_x < xmax:
            # within correct y coordinates
            if ymin < cur_y < ymax:
                if self.target_location == 'checkout':
                    ...
                else:
                    self.next_location()
            else:
                if cur_y < ymin:
                    cur_y += size
                elif cur_y > ymin:
                    cur_y -= ymin
        else:
            diff_to_top = abs(ymin_top - cur_y)
            diff_to_bottom = abs(ymax_bottom - cur_y)

            if diff_to_bottom < diff_to_top:
                if cur_y < ymin_bottom:
                    cur_y += size
                elif cur_y > ymax_bottom:
                    cur_y -= size
                else:
                    if cur_x < tar_x:
                        cur_x += size
                    elif cur_x > tar_x:
                        cur_x -= size
            else:
                if cur_y < ymin_top:
                    cur_y += size
                elif cur_y > ymax_top:
                    cur_y -= size
                else:
                    if cur_x < tar_x:
                        cur_x += size
                    elif cur_x > tar_x:
                        cur_x -= size

        self.current_coordinates = (cur_x, cur_y)

    def next_location(self):
        '''
        Method of the Customer class to select next target_location.

        # ==> Needs to be called, which could be done by storing each created customer object in a list.
        '''
        if self.target_location != 'checkout' and self.finished == False:
            self.target_location = np.random.choice(list(
                self.trans_p_matrix.index), p=list(self.trans_p_matrix[self.target_location]))
            self.target_coordinates = get_semi_random_coord(
                self.target_location)

            # return self.location or 'return location?'
            # - do we need this, or will other functions just make use of customers location to display object appropiately?

        else:
            self.finished = True
            ''' => Delete coordinates to make customer disappear?
            Or just delete customer from instore list (based on finished = True),
            which defines what is displayed'''
