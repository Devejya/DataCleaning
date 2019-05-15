import pandas as pd

pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

df=pd.read_excel('MostValuableSKU-Time-Price.xlsx', header=0, sheet_name='NaNvalues')

print (df.count())


