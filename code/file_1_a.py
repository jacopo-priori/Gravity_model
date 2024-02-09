import pandas as pd
import numpy as np 
import statsmodels.api as sm


chunks = pd.read_csv('data\Gravity_V202211.csv', chunksize=2000)
dfs = [] # filter dataframes
for chunk in chunks:
    df_grav = pd.DataFrame(chunk)
    df_grav_1 = df_grav.loc[:, ['year','iso3_o', 'iso3_d', 'country_exists_o', 'country_exists_d', 'distw_arithmetic', 'gdp_ppp_pwt_o', 'gdp_ppp_pwt_d', 'tradeflow_baci', 'comlang_ethno', 'col_dep_ever', 'sibling_ever', 'contig']]  # selection of relevant variables
    df_grav_2 = df_grav_1[(df_grav_1['country_exists_o'] != 0) & (df_grav_1['country_exists_d'] != 0)]  # keep only observations where both countries existed
    df_grav_3 = df_grav_2.dropna(axis=0, how='any') # drop na
    df_grav_4 = df_grav_3[(df_grav_3['year'] > 2000)] # filter for years
    dfs.append(df_grav_4)
df = pd.concat(dfs)

print(df.head()) 
print(df.describe()) 

df[['gdp_o', 'gdp_d', 'distw_arithmetic', 'tradeflow_baci']] = np.log(df[['gdp_ppp_pwt_o', 'gdp_ppp_pwt_d', 'distw_arithmetic', 'tradeflow_baci']]) # convert to log scale
