import pandas as pd

col = ["Order Id","Product", "Quantity Ordered", "Price Each","Order Date","Street","City","Zip"]
df = pd.read_csv( 'sales_data.csv',names=col,header=0)
print(df)

df["Purchase Date"] = df['Street']+df['City']+df['Zip']
df.drop(columns=["Street","City","Zip"],inplace=True)
print(df)
df.dropna(subset=["Order Id","Product"], inplace=True) # drops either Order Id or Product is Null

mean_price = df.groupby("Product")["Price Each"].transform("mean") # transform is calculating avg but brodacasting the avg to match the size 
# of DF, giving same avg for all grouped col values
print(mean_price)
df["Price Each"] = df["Price Each"].fillna(mean_price)
print(df)
print(df.dtypes)  # Order Date is str type
# converting it into proper Date type
df["Order Date"] = pd.to_datetime(df["Order Date"], format = "mixed")
print(df.dtypes)


# calculating new col total sales = quantity*price both are already of type float
df["Total Sales"] = df["Quantity Ordered"] * df["Price Each"]
print(df)
# grouping by month to find total  revenue per month
# first extracting the month from Order Date
df["Month"] = df["Order Date"].dt.month  # dt lets access datetime properties
print(df)
monthly_rev = df.groupby("Month")["Total Sales"].sum().reset_index(name="Monthly Revenue")  # reset_index gives custom name to agg col
print("Monthly Revenue")
print(monthly_rev)

# finding best selling product by quantity for each month
monthly_sales = (df.groupby(["Month", "Product"])["Quantity Ordered"].sum().reset_index(name="Monthly quantity")) # we have qunatity of each product each month
print("Monthly Sales")
print(monthly_sales)


# finding largest quantity each month
##  best_selling = monthly_sales.groupby('Month')["Monthly quantity"].max() here we want index ,then we will take Product with these index
# the max value is of no use
# then with loc[index] we will get our product
#  #idxmax gives first occurence of same max value
best_selling = monthly_sales.loc[monthly_sales.groupby('Month')["Monthly quantity"].idxmax()]
print(best_selling)


# saving cleaned datasets
df.to_csv('cleaned_sales.csv', index=False)