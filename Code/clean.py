import pandas as pd
df = pd.read_csv('C:/Users/hvtra/OneDrive/Documents/BI/BI Dataset/Automobile data.csv')

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

# print("Add duplicate data")
# new_row = {'Brand Name': 'Tesla', 'Fuel type': 'Electric', 'Aspiration': 'N/A',
#            'Door Panel': '4', 'Design': 'Sedan', 'Wheel Drive': 'AWD',
#            'Engine Location': 'Front', 'Engine Type': 'Electric',
#            'Cylinder Count': 'N/A', 'Engine Size': 'N/A', 'Fuel System': 'N/A',
#            'Bore': 'N/A', 'Stroke': 'N/A', 'Compression Ratio': 'N/A',
#            'Horse Power': '350', 'Top-RPM': 'N/A', 'City Mileage': '130',
#            'Highway Mileage': '140', 'Price in Dollars': '50000'}
# new_row_df = pd.DataFrame(new_row, index=[len(df)])
# df= pd.concat([df, new_row_df], ignore_index=True)

# new_row2 = {'Brand Name': 'Tesla', 'Fuel type': 'Electric', 'Aspiration': 'N/A',
#            'Door Panel': '4', 'Design': 'Sedan', 'Wheel Drive': 'AWD',
#            'Engine Location': 'Front', 'Engine Type': 'Electric',
#            'Cylinder Count': 'N/A', 'Engine Size': 'N/A', 'Fuel System': 'N/A',
#            'Bore': 'N/A', 'Stroke': 'N/A', 'Compression Ratio': 'N/A',
#            'Horse Power': '350', 'Top-RPM': 'N/A', 'City Mileage': '130',
#            'Highway Mileage': '140', 'Price in Dollars': '50000'}
# new_row2_df = pd.DataFrame(new_row2, index=[len(df)])
# df= pd.concat([df, new_row2_df], ignore_index=True)

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

# print(df.columns)

# Count the number of Audi cars in the dataframe
audi_count = df['Brand Name'].value_counts()['audi']

# Print the count
print(f'There are {audi_count} Audi cars in the dataset.')

# Filter rows with the brand 'Isuzu'
isuzu_df = df[df['Brand Name'] == 'Isuzu']

# Display all columns with brand 'Isuzu'
print(isuzu_df)