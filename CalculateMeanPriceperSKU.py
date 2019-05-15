#import required libraries
import pandas as pd

#filename.
f='MostValuableSKU.xlsx'

#read in the data from the sheets of the excel file into dataframes
dfs_1=pd.read_excel(f,sheet_name='straw-1',header=0, parse_dates=['DELV_DT'])
dfs_2=pd.read_excel(f,sheet_name='straw-2',header=0, parse_dates=['DELV_DT'])
dfs_3=pd.read_excel(f,sheet_name='straw-3',header=0, parse_dates=['DELV_DT'])
dfba_1=pd.read_excel(f,sheet_name='black-1',header=0, parse_dates=['DELV_DT'])
dfba_2=pd.read_excel(f,sheet_name='black-2',header=0, parse_dates=['DELV_DT'])
dfba_3=pd.read_excel(f,sheet_name='black-3',header=0, parse_dates=['DELV_DT'])
dfbu_1=pd.read_excel(f,sheet_name='blue-1',header=0, parse_dates=['DELV_DT'])
dfbu_2=pd.read_excel(f,sheet_name='blue-2',header=0, parse_dates=['DELV_DT'])
dfbu_3=pd.read_excel(f,sheet_name='blue-3',header=0, parse_dates=['DELV_DT'])
dfr_1=pd.read_excel(f,sheet_name='rasp-1',header=0, parse_dates=['DELV_DT'])
dfr_2=pd.read_excel(f,sheet_name='rasp-2',header=0, parse_dates=['DELV_DT'])
dfr_3=pd.read_excel(f,sheet_name='rasp-3',header=0, parse_dates=['DELV_DT'])
dfc_1=pd.read_excel(f,sheet_name='cherries-1',header=0, parse_dates=['DELV_DT'])
dfc_2=pd.read_excel(f,sheet_name='cherries-2',header=0, parse_dates=['DELV_DT'])
dfc_3=pd.read_excel(f,sheet_name='cherries-3',header=0, parse_dates=['DELV_DT'])

print ('mean straw_1 = ', dfs_1['price_per_unit'].mean())
print ('mean straw_2 = ', dfs_2['price_per_unit'].mean())
print ('mean straw_3 = ', dfs_3['price_per_unit'].mean())
print ('mean black_1 = ', dfba_1['price_per_unit'].mean())
print ('mean black_2 = ', dfba_2['price_per_unit'].mean())
print ('mean black_3 = ', dfba_3['price_per_unit'].mean())
print ('mean blue_1 = ', dfbu_1['price_per_unit'].mean())
print ('mean blue_2 = ', dfbu_2['price_per_unit'].mean())
print ('mean blue_3 = ', dfbu_3['price_per_unit'].mean())
print ('mean rasp_1 = ', dfr_1['price_per_unit'].mean())
print ('mean rasp_2 = ', dfr_2['price_per_unit'].mean())
print ('mean rasp_3 = ', dfr_3['price_per_unit'].mean())
print ('mean cherries_1 = ', dfc_1['price_per_unit'].mean())
print ('mean cherries_2 = ', dfc_2['price_per_unit'].mean())
print ('mean cherries_3 = ', dfc_3['price_per_unit'].mean())
