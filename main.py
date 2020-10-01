import numpy as np
import cv2
import time
import pandas as pd

from customer_class import Customer
from probabilities import get_trans_prob_matrix, get_prob_for_new_customer_list
from supermarket import Supermarket


def generate_new_customer(global_instore_count: int, cust_prob_list: list):
    '''
    Decides base on customer currently in store and probability list if new customer is created or not.
    If yes, then creates new instore customer.

    Parameters
    ----------
    global_instore_count : INT
        DESCRIPTION.
    cust_prob_list : list
        DESCRIPTION.

    '''
    
    prob = cust_prob_list[global_instore_count]
    generate = np.random.choice(['yes', 'no'], p=(prob, 1-prob))
    
    if generate == 'yes': 
        '''customer_image = sth random'''
        #global instore_customers
        instore_customers.append(Customer(tpm, customer_image))
        #updating instore_count
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


market = Supermarket(market_img, [])

while True:
    frame = market_img.copy()
    market.draw(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
