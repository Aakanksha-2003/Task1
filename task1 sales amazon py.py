import pandas as pd

# step 1:Load the dataset
df = pd.read_csv("amazon.csv")

# Display the first 5 rows
print(df.head())

#step 2:Inspect the dataset
print(df.info())
print(df.head())

#step 3: Handle Missing Values
#Check for missing values:

print(df.isnull().sum())

#Drop or fill:
df = df.dropna()  # Or use df.fillna("Unknown") if needed

# step 4: Remove Duplicates
df = df.drop_duplicates()

# step 5: Clean Column Headers
#Convert all headers to lowercase and replace spaces:
df.columns = df.columns.str.lower().str.replace(" ", "_")

#step 6: Standardize Formats
#Clean and convert discounted_price, actual_price, discount_percentage, and rating_count:

df["discounted_price"] = df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["actual_price"] = df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)

#Convert rating to float:

df["rating"] = pd.to_numeric(df["rating"], errors='coerce')

#step 7: Check & Fix Data Types

print(df.dtypes)
# If needed, convert columns explicitly:
# df['some_column'] = df['some_column'].astype(int)

#step 8: (Optional) Convert Dates
#If there are date columns (e.g., "rating"):
    
df["rating"] = pd.to_datetime(df["rating"], dayfirst=True)

#step 9: Save Cleaned Data
df.to_csv("amazon_cleaned.csv", index=False)