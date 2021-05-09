import numpy as np
import pandas as pd
df = pd.read_csv('NISPUF17.csv', index_col=0)
n_df = df[['HAD_CPOX', 'P_NUMVRC']]
def corr_chickenpox():
    n_df_2 = n_df.where(n_df['HAD_CPOX'] < 3).dropna()
    print(n_df_2)


    # here is some stub code to actually run the correlation
    

corr_chickenpox()

import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.read_csv('NISPUF17.csv', index_col=0)
n_df = df[['HAD_CPOX', 'P_NUMVRC']]

def corr_chickenpox():
    
    n_df_2 = n_df.where(n_df['HAD_CPOX'] < 3).dropna()
    print(n_df_2)

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(n_df_2["HAD_CPOX"],n_df_2["P_NUMVRC"])
    
    # just return the correlation
    #return corr

    # YOUR CODE HERE
    raise corr

print(corr_chickenpox())