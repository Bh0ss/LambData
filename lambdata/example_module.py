""""LambData -- A collection of Data Science helper functions"""

import pandas as pd 
import numpy as np

FAVORITE_ANIMALS = ['cat', 'dog','slot','albino giraffe','reversed zebra']
Test_df = pd.DataFrame(np.random.randint(0,100,size=(15, 4)), columns=list('ABCD'))
def df_cleaner(df):
    """"Cleans DF"""
    #todo implement a function to clean dataframe
    df = df.copy()
    is_null = df.isnull().values.any()

    return df

