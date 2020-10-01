from Customer import Customer
import numpy as np
import random

import trans_prob_matrix


size = 32
cust_img = np.zeros((size, size, 3), dtype='int8')
aisle_names = ['drinks', 'dairy', 'spices', 'fruit', 'checkout']
aisles = {
    'drinks': {'x': (100, 230-size), 'y': (170, 470-size)},
    'dairy': {'x': (340, 460-size), 'y': (170, 470-size)},
    'spices': {'x': (570, 690-size), 'y': (170, 470-size)},
    'fruit': {'x': (800, 920-size), 'y': (170, 470-size)},
    'checkout': {'x': (200, 430-size), 'y': (650, 750-size)}
}


class Supermarket:
    def __init__(self, image, customers):
        self.image = image
        self.customers = customers

    def __repr__(self):
        return f"Supermarket that currently has {len(self.customers)}."

    def draw(self, frame):
        for customer in self.customers:
            section = customer.current_location
            xmin, xmax = aisles[section]['x']
            ymin, ymax = aisles[section]['y']
            x = random.randint(xmin, xmax)
            y = random.randint(ymin, ymax)
            self.image[y:y+size, x:x+size] = cust_img

    # def drawx(self, frame):
    #     """draws n_customers onto the frame"""
    #     cust = np.zeros((size, size, 3), dtype='int8')
    #     for aisle in aisle_names:
    #         xmin, xmax = aisles[aisle]['x']
    #         ymin, ymax = aisles[aisle]['y']
    #         x = random.randint(xmin, xmax)
    #         y = random.randint(ymin, ymax)
    #         self.image[y:y+size, x:x+size] = cust


# class Location:

#     def __init__(self, name, x, y, n_customers=0):
#         self.name = name,
#         self.x = x,
#         self.y = y,
#         self.n_customers = n_customers

#     def __repr__(self):
#         return f"Location {self.name} has coordinates x={self.x} and y={self.y} and currently has {self.n_customers}."
