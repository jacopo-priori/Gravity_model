### PACKAGES

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt

### DATAFRAME

chunks = pd.read_csv('\Gravity_V202211.csv', chunksize=2000)
dfs = [] 
for chunk in chunks: # filter dataframes
    df_grav = pd.DataFrame(chunk)
    df_grav_1 = df_grav.loc[:, ['year','country_id_o', 'country_id_d', 'country_exists_o', 'country_exists_d', 'distw_harmonic', 'gdp_ppp_pwt_o', 'gdp_ppp_pwt_d', 'tradeflow_baci', 'comlang_ethno', 'heg_o', 'heg_d', 'sibling_ever', 'contig']]  # selection of relevant variables
    df_grav_2 = df_grav_1[(df_grav_1['country_exists_o'] != 0) & (df_grav_1['country_exists_d'] != 0)]  # keep only observations where both countries existed
    df_grav_3 = df_grav_2.dropna(axis=0, how='any') # drop na
    df_grav_4 = df_grav_3[(df_grav_3['year'] >= 1997)] # filter for years
    dfs.append(df_grav_4)
df = pd.concat(dfs)

print(df.head(20)) 
print(df.describe()) 

df[['gdp_o_log', 'gdp_d_log', 'dist_log', 'tf_log']] = np.log(df[['gdp_ppp_pwt_o', 'gdp_ppp_pwt_d', 'distw_harmonic', 'tradeflow_baci']]) # add logged values for regressions

### GDP CHART

df_gdp = df[['year','country_id_o','gdp_ppp_pwt_o']].drop_duplicates() # only select one observations per country per year as GDP is the same
df_gdp = df_gdp.groupby('year')['gdp_ppp_pwt_o'].sum().reset_index() # sum GDP's per year
print(df_gdp.head(20))
print(df.describe()) 

plt.plot(df_gdp['year'], df_gdp['gdp_ppp_pwt_o']) # plot world GDP
plt.xlabel('Year')
plt.ylabel('Log of sum of deflated GDP at current PPP in 2011 thousands USD')
plt.yscale('log') # log scale
plt.title('World GDP over time')
plt.show()

### TRADEFLOW CHART *to be revised*

df_tf = df[['year','country_id_o', 'country_id_d', 'tradeflow_baci']]
df_tf[['country_id_o', 'country_id_d']] = pd.DataFrame(np.sort(df_tf[['country_id_o', 'country_id_d']].values, axis=1), index=df.index) 
df_tf = df_tf.drop_duplicates(subset=['country_id_o', 'country_id_d']) # drop one observation in each pair of observations where the only difference is the direction of trade
print(df_tf.describe())
print(df_tf.head(20))

plt.plot(df_tf['year'], df_tf['tradeflow_baci'])# plot world tradeflow
plt.xlabel('Year')
plt.ylabel('lorem ipsum')
plt.yscale('log') # log scale
plt.title('World trade flow over time')
plt.show()
