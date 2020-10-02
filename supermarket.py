import numpy as np
import random


class Supermarket:
    def __init__(self, image, size):
        self.image = image
        self.size = size

    def __repr__(self):
        return f"Supermarket"

    def draw(self, customers):
        self.frame = self.image.copy()
        for customer in customers:
            x, y = customer.current_coordinates
            self.frame[y:y+self.size, x:x+self.size] = customer.icon
