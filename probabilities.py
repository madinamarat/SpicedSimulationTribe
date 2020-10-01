# -*- coding: utf-8 -*-
"""
Reads the five day-of-week supermarket csvs,
calculates the Transition Probability Matrix from it and
returns the matrix as a dataframe
with current location as columns headers and next possible location as index.
Stores it as csv in <wd>/data and will first look to load it from there when 
called again.

Generates the list of probabilities used for the generate_new_customer function.


Can be used by
--------------
   from trans_prob_matrix import get_trans_prob_matrix, get_prob_for_new_customer_list

"""
import pandas as pd
import numpy as np
import os




def read_five_days():
    '''
    Reads the five csv of the supermarket dataset and returns them within
    one dataframe, with customer_no adjusted for respective day-of-week.
    '''
    dirname = './data/'
    files = [f for f in os.listdir(dirname) if f.endswith('.csv')]

    dfs = []
    for f in files:
        day = f[:-4]
        df = pd.read_csv(dirname + f, sep=';')
        df['customer_no'] = day + '_' + df['customer_no'].astype(str)
        dfs.append(df)

    df = pd.concat(dfs)

    df.reset_index(inplace = True)
    df.drop(columns='index', inplace=True)

    return df



def ts_to_datetime_index(df):
    df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index('timestamp', inplace=True)

    return df


def transform(df):

    df = df.copy()

    # Add missing timeslots for each customer & add 'prev_location'
    df = df.groupby('customer_no')[['location']].resample(rule='60S').ffill()
    df['prev_location'] = df['location'].shift()

    # Clean 'prev_location' column
    mask1 = df['prev_location'] == 'checkout'
    mask2 = df['location'] != 'checkout'
    df.loc[mask1 & mask2, 'prev_location'] = np.nan
    df['prev_location'].fillna('entrance', inplace=True)

    return df


def tpm_from_df(df):

    TPM = pd.crosstab(df['location'], df['prev_location'], normalize=1)

    return TPM


def get_trans_prob_matrix():
    '''
    Uses the above functions to read the five supermarket datasets
    and to return a transition probability matrix used to for the
    Customer class function change_location.
    '''
    try:
        trans_prob_matrix = pd.read_csv("data/trans_prob_matrix.csv", index_col = 0)

    except FileNotFoundError:

        df = read_five_days()
        df = ts_to_datetime_index(df)
        df = transform(df)
        trans_prob_matrix = tpm_from_df(df)

        trans_prob_matrix.to_csv("data/trans_prob_matrix.csv")

    return trans_prob_matrix


def get_prob_for_new_customer_list():
    '''
    - Generates and returns a list of probabilities if a new customer is generated,
    based on the current numbers of customers in the store.
    - Assumes a maximum number of customers instore of 36.
    - The probability to generate new customer is below 50% once 12 customers are in the store
    (based on the mean instore customer number on wednesday dataset).
    '''
    
    # range of possible numbers of customer in store: 0 to maximum of 36
    raw = []
    for i in range(37):
        raw.append(i)
    
    raw_normed = [float(i)/len(raw) for i in raw]
    
    probability_list = []
    a = 0.2
    for i in raw_normed:
        new = i * a
        probability_list.append(new)
        a = a**a - 0.05
    
    probability_list.reverse()
    
    return probability_list