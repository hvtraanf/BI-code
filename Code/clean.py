import pandas as pd
df = pd.read_csv('C:/Users/Admin/Documents/ASM/BI-code/BI Dataset/Automobile data.csv')

# print("Original Dataset")
# print(df.head(10))

# print("Shape of the dataset")
# print(df.describe())

# print("Columns of the dataset")
# print(df.columns)

# print("Dropping columns")
# df = df.loc[:, ~df.columns.str.contains('^Fuel')]

# print("Columns of the dataset")
# print(df.columns)

# print("Add Test Column to dataset")
# for i in range(len(df)):
#     for j in range(10):
#         df.loc[i, "Test"] = i + j

# print("New Dataset")
# print(df.head(10))


# print("Check for duplicate rows")
# print(df.duplicated())

# df.drop_duplicates(inplace=True)

# print("Check for duplicate rows")
# print(df.duplicated())

# print(df.dtypes)

# # Convert the columns to float type
# df['City Mileage'] = df['City Mileage'].astype(float)
# df['Highway Mileage'] = df['Highway Mileage'].astype(float)
# df['Price in Dollars'] = df['Price in Dollars'].astype(float)

# print("new data types")
# print(df.dtypes)

# print(df.head(10))

print(df.columns)

# Count the number of Audi cars in the dataframe
audi_count = df['Brand Name'].value_counts()['audi']

# Print the count
print(f'There are {audi_count} Audi cars in the dataset.')

# Create a list of dictionaries for Tesla cars
# tesla_models = [
#     {
#         'Brand Name': 'Tesla',
#         'Fuel type': 'Electric',
#         'Aspiration': 'Std',  # Replacing 'Standard' with 'Std'
#         'Door Panel': 4,  # Number of doors for Model S
#         'Design': 'Sedan',  # Sedan design for all Tesla models
#         'Wheel Drive': 'AWD',
#         'Engine Location': 'Front',
#         'Engine Type': 'Electric',
#         'Cylinder Count': None,
#         'Engine Size': None,
#         'Fuel System': 'Electric',
#         'Bore': None,
#         'Stroke': None,
#         'Compression Ratio': None,
#         'Horse Power': 500,
#         'Top-RPM': None,
#         'City Mileage': 90,
#         'Highway Mileage': 110,
#         'Price in Dollars': 90000
#     },
#     {
#         'Brand Name': 'Tesla',
#         'Fuel type': 'Electric',
#         'Aspiration': 'Std',  # Replacing 'Standard' with 'Std'
#         'Door Panel': 4,  # Number of doors for Model 3
#         'Design': 'Sedan',  # Sedan design for all Tesla models
#         'Wheel Drive': 'AWD',
#         'Engine Location': 'Front',
#         'Engine Type': 'Electric',
#         'Cylinder Count': None,
#         'Engine Size': None,
#         'Fuel System': 'Electric',
#         'Bore': None,
#         'Stroke': None,
#         'Compression Ratio': None,
#         'Horse Power': 300,
#         'Top-RPM': None,
#         'City Mileage': 100,
#         'Highway Mileage': 120,
#         'Price in Dollars': 60000
#     }
# ]

# # Convert the list of dictionaries to a DataFrame
# tesla_df = pd.DataFrame(tesla_models)

# # Concatenate the original DataFrame with the Tesla DataFrame
# df = pd.concat([df, tesla_df], ignore_index=True)

# # Replace empty values with 'N/A'
# df.fillna('N/A', inplace=True)

# Replace "gas" with "petrol" in the "Fuel type" column
df['Fuel type'].replace('gas', 'petrol', inplace=True)

# Save the updated DataFrame to a new CSV file
# df.to_csv("C:/Users/Admin/Documents/ASM/BI-code/BI Dataset/Automobile data.csv", index=False)

# Add a new column named 'Test' with the value "test" for all rows
df['Test'] = 'test'
print(df.columns)

df.drop(columns='Test', inplace=True)
print(df.columns)

# Filter out rows where both conditions are met using boolean indexing
filtered_df = df[(df['Fuel type'] == 'petrol') & (df['Price in Dollars'] > 20000)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv("filtered_file.csv", index=False)
ft_df = pd.read_csv('filtered_file.csv')
print(ft_df.head())

# Function to calculate the 25th and 75th percentiles for a series
def percentiles(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    return Q1, Q3

# Function to calculate the IQR for a series
def iqr(series):
    Q1, Q3 = percentiles(series)
    IQR = Q3 - Q1
    return Q1, Q3, IQR

# Remove outliers from the 'Price in Dollars' column
Q1, Q3, IQR = iqr(df['Price in Dollars'])
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_cleaned = df[(df['Price in Dollars'] >= lower_bound) & (df['Price in Dollars'] <= upper_bound)]


# Save the cleaned dataset
df_cleaned.to_csv("cleaned_data_by_brand.csv", index=False)