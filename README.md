# DataCleaning
Using pandas to clean and prepare loblaw's data for analysis

What I learned?
1) Pandas
2) Exporting dataframes to Excel sheets

What do the following files do?
1) SKUpriceswithDates(timeseries) : From the MostValuableSKU.xlxs file, takes the transaction records for all most valubale SKUs from different sheets to merge them all together. Then changing the date frequency to daily and putting them all together in a sheet and exporting that to an excel sheet.
2) timeseriesdiffdates.py : Returns a plot which compares the prices of one SKU wrt another SKU over time
3) append_df_to_excel.py : The function provides us a way to append pandas dataframes to existing (If not existing, it will make a new one) excel file/sheets.
4) CalculateMeanPriceperSKU.py : prints mean price per SKU using the Most valuable SKU dataframe
5) Count non zeroes in col.py : prints number of non zero entries in a particular column in dataframe
7) PandasBasicBerrieCherries.py : From the data provided by loblaws, identifies the most valuable SKUs and appends those dataframes to a new excel file.
