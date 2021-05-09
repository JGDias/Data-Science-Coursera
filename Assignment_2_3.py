import pandas as pd

df = pd.read_csv('NISPUF17.csv', index_col=0)
n_df = df[['HAD_CPOX','P_NUMVRC','SEX']]
n_df_2 = n_df.where(n_df['P_NUMVRC']>0).dropna()

def chickenpox_by_sex():
    info = {}
    for i in [1,2]:
        mask_1 = (df['SEX'] == i)
        n_df_3 = n_df_2.where(mask_1).dropna()
        X1 = n_df_3.where(n_df_3['HAD_CPOX'] == 1).count()['SEX']
        X2 = n_df_3.where(n_df_3['HAD_CPOX'] == 2).count()['SEX']
        if i == 1:
            info['male'] = X1/X2
        else:
            info['female'] = X1/X2
    return info

chickenpox_by_sex()