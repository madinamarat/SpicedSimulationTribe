# -*- coding: utf-8 -*-
"""
Read the five day-of-week supermarket csvs,
calculates the Transition Probability Matrix from it and
returns the matrix as a dataframe
with current location as columns headers and next possible location as index.

Can be used by
--------------
    import trans_prob_matrix

    tpm = trans_prob_matrix.get_tpm()


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


def get_tpm():
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
