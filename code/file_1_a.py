import pandas as pd
import numpy as np 
import statsmodels.api as sm

df = pd.read_csv('C:\\Users\\HP\\Desktop\\gravity\\Gravity_V202211.csv', index_col=0)
df = pd.DataFrame(df)

df_1 = df.loc[:, ['country_o', 'country_d', 'country_exists_o', 'country_exists_d', 'distw_arithmetic', 'gdp_o', 'gdp_d', 'tradeflow_baci', 'commlang_ethno', 'col_dep_ever', 'sibling_ever', 'contig']]  # selection of relevant variables
df_2 = df_1[(df_1['country_exists_o'] != 0) & (df_1['country_exists_d'] != 0)]  # keep only observations where both countries existed
df_3 = df_2.dropna(axis=0, how='any') # drop na
df_3[['gdp_o', 'gdp_d', 'distw_arithmetic', 'tradeflow_baci']] = np.log(df_3[['gdp_o', 'gdp_d', 'distw_arithmetic', 'tradeflow_baci']]) # convert to log scale


