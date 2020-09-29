""""LambData -- A collection of Data Science helper functions"""

import pandas as pd 
import numpy as np

# Test DF
Test_df = pd.DataFrame(np.random.randint(0,100,size=(15, 4)),
                         columns=list('ABCD'))

class CleanDataFrame:
    '''
    Allows you to remove nulls and clean headers
    '''
    def df_cleaner(df):
        """"Cleans DF by creating copy 
            then checking for nulls
        """
        # Todo implement a function to clean dataframe
        # Create copy of dataframe not to mess with original
        df = df.copy()
        # Check dataframe for nulls 
        is_null = df.isnull().values.any()
        return df
    def CleaningHeaders(df):
        '''
        Removes any weird character and leading and trailing space
        from a dataframe
        '''
        # Clean dataframe headers
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        return df