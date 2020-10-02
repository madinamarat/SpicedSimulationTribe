import numpy as np
import cv2
import time
import pandas as pd
import random

from supermarket import Supermarket
from customer_class import Customer
from probabilities import get_trans_prob_matrix, get_prob_for_new_customer_list
import customer_images

size = 32
# cust_img = np.zeros((size, size, 3), dtype='int8') # static image


def generate_new_customer(global_instore_count: int, cust_prob_list: list):
    '''
    Decides based on customers currently in store and probability list if new customer is created or not.
    If yes, then creates new instore customer.

    Parameters
    ----------
    global_instore_count : INT
        Number of customers currently in the store.
    cust_prob_list : list
        List of the probabilities that a new customer is created to enter the store,
        dpendent on number of customers currently in the store, the latter
        equals Index of the list.

    '''

    prob = cust_prob_list[global_instore_count]
    generate = np.random.choice(['yes', 'no'], p=(prob, 1-prob))

    if generate == 'yes':
        # customer_image = customer_images.get_random_image()
        customer_image = customer_images.pacman4
        #global instore_customers
        instore_customers.append(Customer(tpm, customer_image))
        # updating instore_count
        global instore_count
        instore_count = len(instore_customers)


def hello_supermarket():
    '''
    Start-up function. 
    Generates global variables
    - prob_for_new_customer_list
    - instore_customers list
    - instore_count
    - tpm : transition probability matrix via get_tpm
    and creates starting population of customers for supermarket generation.
    '''

    global instore_customers, instore_count, prob_for_new_customer_list, tpm
    instore_customers = []
    instore_count = 0
    prob_for_new_customer_list = get_prob_for_new_customer_list()
    tpm = get_trans_prob_matrix()

    for _ in range(20):
        generate_new_customer(instore_count, prob_for_new_customer_list)


hello_supermarket()
market_img = cv2.imread('./img/market.png')
market = Supermarket(market_img, size)

while True:
    time.sleep(0.1)
    old_count = instore_count
    market.draw(instore_customers)
    instore_customers = [
        cust for cust in instore_customers if cust.finished == False]
    instore_count = len(instore_customers)
    for x in range(old_count - instore_count):
        generate_new_customer(instore_count, prob_for_new_customer_list)
        generate_new_customer(instore_count, prob_for_new_customer_list)
    [cust.move() for cust in instore_customers]
    cv2.imshow('frame', market.frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
