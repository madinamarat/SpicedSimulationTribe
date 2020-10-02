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
        dependent on number of customers currently in the store, the latter
        equals Index of the list.

    '''

    prob = cust_prob_list[global_instore_count]
    generate = np.random.choice(['yes', 'no'], p=(prob, 1-prob))

    if generate == 'yes':
        customer_image = customer_images.get_random_image()
        # customer_image = customer_images.pacman4
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
    - total_visits_abs : dict to store visits of a location (incl. multiple by same customer)
    - revenue_per_visit : dict that contains constant values of avg revenue per visit for calculation
    - total_revenue_eur : dict to store calculated total revenue per location, in Euro

    and creates starting population of customers for supermarket generation.
    '''

    global instore_customers, instore_count, prob_for_new_customer_list, tpm, outstore_customers
    instore_customers = []
    instore_count = 0
    prob_for_new_customer_list = get_prob_for_new_customer_list()
    tpm = get_trans_prob_matrix()
    outstore_customers = []

    global revenue_per_visit, total_revenue_eur
    revenue_per_visit = {'dairy': 5, 'drinks': 6, 'fruit': 4, 'spices': 3}
    total_revenue_eur = {'dairy': 0, 'drinks': 0,
                         'fruit': 0, 'spices': 0, 'total': 0}

    for _ in range(20):
        generate_new_customer(instore_count, prob_for_new_customer_list)


def calculate_revenue(total_revenue, customers_out):
    '''
    Takes this loop's outstore_customers list to add the revenue of the customers
    visits and add it to the total_revenue_eur dict.
    Then cleans the outstore_customers for the next loop.
    '''
    for cust in customers_out:
        for key in revenue_per_visit:
            rev = (cust.visits[key] * revenue_per_visit[key])
            total_revenue[key] += rev
            total_revenue['total'] += rev

    print(total_revenue)
    global outstore_customers
    customers_out = []


hello_supermarket()
market_img = cv2.imread('./img/market.png')
market = Supermarket(market_img, size)

while True:
    time.sleep(0.1)
    old_count = instore_count
    market.draw(instore_customers)
    outstore_customers = [
        cust for cust in instore_customers if cust.finished == True]
    instore_customers = [
        cust for cust in instore_customers if cust.finished == False]
    instore_count = len(instore_customers)
    for x in range(old_count - instore_count):
        generate_new_customer(instore_count, prob_for_new_customer_list)
        generate_new_customer(instore_count, prob_for_new_customer_list)
    [cust.move() for cust in instore_customers]
    cv2.imshow('frame', market.frame)
    if (len(outstore_customers) > 0):
        calculate_revenue(total_revenue_eur, outstore_customers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
