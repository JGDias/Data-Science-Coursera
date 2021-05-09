
import pandas as pd
def proportion_of_education():
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    for i in range(len(df)):
        x = df.loc[i+1, 'EDUC1']
        if x == 4:
            c4 += 1
        elif x == 3:
            c3 += 1
        elif x == 2:
            c2 += 1
        else:
            c1 += 1

    info = {"less than high school":c1/len(df),
    "high school":c2/len(df),
    "more than high school but not college":c3/len(df),
    "college":c4/len(df)}
    return info
print(proportion_of_education().keys())
