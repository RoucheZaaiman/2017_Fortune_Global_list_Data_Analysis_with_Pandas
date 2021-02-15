# In these project based exercises in Python Pandas selected fundamental to intermediate Pandas
# operations are applied to do calculations. The Fortune Global 500 list from 2017 dataframe is
# used for Data Analysis.  

# Fundamental Pandas operations and calculations in these project based exercises are as follows:  
# * Selecting and slicing rows and columns or selecting specific values in Pandas using column names.
# * Selecting items from a Series by label.
# * Vectorized operations
# * Using Boolean arrays in Pandas to enable better data analysis e.g. determining in which country
# each of the companies in the motor industry are.

# Intermediate operations and calculations in Python Pandas are as follows:  
# * Combining Boolean comparisons for more complex data analysis e.g. finding companies that have a large
# revenue but have negative profits and determining which companies are in the Technology sector but outside
# of the USA.
# * Sorting values and using integer location to find a specific value or string e.g. determining the name of
# the company that has the most employees or displaying the name of the top Japanese employer.
# * Using aggregation (loops in Pandas) to perform advanced data analysis, e.g. finding the top employer from
# each country or the companies from each sector that produces the biggest return on assets (ROA).

#These Pandas exercises ware done through DataQuest and they also provided the dataset f500.csv.


import pandas as pd

# Reading the CSV File:

f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None


# f500 data Shape, type of Dataframe and General Information about our Dataframe:
f500_type = type(f500)
f500_shape = f500.shape

f500_head = f500.head(5)
f500_tail = f500.tail(4)

f500.info()


# Selecting a Column From a DataFrame by Label:

# Selecting the Industries Column
industries = f500.loc[:, "industry"]
# Datatype of the Industries Column
industries_type = type(industries)
# Selecting the Countries Column
countries = f500["country"]
# Selecting the 'Revenues' and 'Years of Global 500 list' Columns:
revenues_years = f500[["revenues", "years_on_global_500_list"]]
# Selecting all the Columns from 'ceo' to 'Sector'
ceo_to_sector = f500.loc[:, "ceo":"sector"]


# Selecting Rows From a DataFrame by Label:

# Selecting the entry (row) 'Toyota Motor' according to Location:
toyota = f500.loc["Toyota Motor"]
# Selecting the entries (rows) that manufactures Drinks:
drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]
# Selecting the entries (rows) that are located in the middle of the Fortune Global 500 list:
middle_companies = f500.loc["Tata Motors":"Nationwide", "rank":"country"]


# Choosing selected companies (row entries) that have moved up / down with a great number of
#rankings and returning selected columns for these companies
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"], ["rank","previous_rank"]]
# Selecting specific columns for the companies that are at the bottom of the list.
bottom_companies = f500.loc["National Grid":"AutoNation", ["rank","sector","country"]]


# Value Counts Method
# The Value Counts Method gives an output of the number of items there are in each category for
# the selected Column. In this case it will give the number of companies on the Fortune Global 500
# list that is situated in each country
countries = f500["country"]
country_counts = countries.value_counts()


# Selecting Items from a Series by Label:

countries = f500['country']
countries_counts = countries.value_counts()
# india will return the number of companies in India
india = countries_counts["India"]
# north_america returns the number of companies for each of the Selected Countries
north_america = countries_counts[["USA", "Canada", "Mexico"]]


# Vectorized Operations

rank_change = f500["previous_rank"] - f500["rank"]


# Method Chaining
# Finding all the companies that have not been ranked in 2016
zero_previous_rank = f500["previous_rank"].value_counts().loc[0]


# Series Data Exploration Methods: Determine the Min, Max and Descriptive Statistics for a Series:

rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

rank = f500["rank"]
rank_desc = rank.describe()
prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()

# Dataframe Descriptive Statistics returns the descriptive statistics for each column

f500_desc = f500.describe(exclude = numpy.object)
# Returning the row entry that has the highest integer values, i.e. Walmart in this case, having the maximum
# revnue, profits and the moste employees.
max_f500 = f500.max(axis=0, numeric_only=True)


# Assigning values or names etc. to a specific position in the dataframe, using Pandas:

dowf500 = f500.loc[["Dow Chemical"]]
ceof500 = f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"


# Boolean Indexing with pandas Objects
# Returning the corresponding country for each of  companies in the 'Motor Vehicles and Parts' industry
motor_bool = f500["industry"] == "Motor Vehicles and Parts"
motor_countries = f500.loc[motor_bool, "country"]


# Using Boolean Arrays to Assign Values
# Replacing the 0-values in the column 'previous_rank' with NaN using a Boolean Array
import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
# Viewing the change in value counts for previous_rank will show a count of 33 for NaN
prev_rank_after = f500["previous_rank"].value_counts(dropna = False).head()
# Viewing the top 5 entries ranking and revenue changes
f500_selection = f500[["rank", "revenues", "revenue_change"]].head()

# Creating New Columns

f500["rank_change"] = f500["previous_rank"] - f500["rank"]
rank_change_desc = f500["rank_change"].describe()
# Viewing the minimum rank change
minrank_change = rank_change.min()

# Determining the Top Performers by Country
# Viewing the data again:
f500.head()
# Determining the top 2 industries in the USA
country_usa = f500[f500["country"] == 'USA']
industry_usa = country_usa["industry"].value_counts().head(2)
# Determining the top 3 sectors in China
country_china = f500[f500["country"] == 'China']
sector_china = country_china["sector"].value_counts().head(3)
                     

# Selecting data by integer position using iloc
# Selecting the fifth row, i.e. index 4
fifth_row = f500.iloc[4]
# Selcting the company name that is ranked first
company_value = f500.iloc[0,0]

first_three_rows = f500.iloc[:3, : ]
# Selecting the first 7 rows, but displaying only columns 1 -5
first_seventh_row_slice = f500.iloc[[0,6],:5]


#Creating boolean masks in Pandas:
# Displaying the columns 'company', 'rank' and 'previous_rank' of the top 5 companies that had a previous
# rank 0
prev_rank_isnull = f500["previous_rank"].isnull()
df_isnull = f500[prev_rank_isnull]
null_previous_rank = df_isnull[['company','rank','previous_rank']]
top5_null_prev_rank = null_previous_rank.iloc[:5]


# Pandas Index Alignment
# Displaying all the companies that had a ranking in 2016 and 2017
previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank
# Adding the column 'rank_change' to our dataframe
f500["rank_change"] = rank_change


# Combined Boolean Comparisons
# Determining which companies had a large revenue, but had a negative profit in 2017
large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500[combined]

# Displaying companies that are from Brazil or Venzuela
filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]
# Displaying companies in the Technology sector which are not in the USA
sector = (f500["sector"] == "Technology") & ~ (f500["country"] == "USA")
tech_outside_usa = f500[sector].head()


# Sorting Values
# Displaying the name of the top Japanese employer
country_japan = f500[f500["country"] == "Japan"]
sorted_rows = country_japan.sort_values("employees", ascending = False)
first_row = sorted_rows.iloc[0]
top_japanese_employer = first_row.iloc[0]


# Using Loops with pandas
# Determining the top employer from each Country listed on the 2017 Fortune Global 500 list
                                                                     
top_employer_by_country = {}

countries = f500["country"].unique()

for c in countries:
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees", ascending = False)
    first_row = sorted_rows.iloc[0]
    company = first_row.iloc[0]
    
    top_employer_by_country[c] = company

# Determining the company that yielded the greatest Return on Assets for each sector

f500["roa"] = f500["profits"] / f500["assets"]

top_roa_by_sector = {}
sector = f500["sector"].unique()

for s in sector:
    selected_rows = f500[f500["sector"] == s]
        
    sorted_rows = selected_rows.sort_values("roa", ascending = False)
    first_row = sorted_rows.iloc[0]
    company = first_row.iloc[0]
    
    top_roa_by_sector[s] = company

                     




