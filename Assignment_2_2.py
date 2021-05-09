import pandas as pd

df = pd.read_csv('NISPUF17.csv', index_col=0)
n_df = df[['CBF_01','P_NUMFLU']]

def average_influenza_doses():

    rel = []
    for i in [1,2]:
        mask_1 = (df['CBF_01'] == i)
        n_df_2 = n_df.where(mask_1).dropna()
        x = sum(n_df_2['P_NUMFLU'])/len(n_df_2['CBF_01'])
        rel.append(x)
    print(sum(n_df_2['P_NUMFLU'])/len(n_df_2['CBF_01']))
    print(rel)
average_influenza_doses()



