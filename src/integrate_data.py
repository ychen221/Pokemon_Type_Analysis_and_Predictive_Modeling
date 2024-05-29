"""
Integrates all the data into a format that can be easily analyzed
This will probably take the form of merging (joining) several Pandas
DataFrames, or issuing SQL queries over tables in a relational DB.

Author: < Student Name >
"""
import pandas as pd

# Load the dataset
source1_df = pd.read_csv('../data/processed/cleaned_source1_scraped_data.csv')
source2_df = pd.read_csv('../data/processed/cleaned_source2_scraped_data.csv')
source3_df = pd.read_csv('../data/processed/cleaned_source3_static_data.csv')

# join the source2_df and source3_df

## first convert source3_df Name column's values to lowercase
source3_df['Name'] = source3_df['Name'].str.lower()
# Perform an inner join to keep only matching entries
matching_df = pd.merge(source2_df, source3_df, left_on='Name', right_on='Name', how='inner')


# join source1_df with the matching_df
df = pd.merge(matching_df, source1_df, left_on='Name', right_on='Name', how='outer')
# replace Nan with 0
df.fillna(0, inplace=True)
#replace False as 0 True as 1
df.replace({False: 0, True: 1}, inplace=True)

# Define the output path for the cleaned CSV file
output_path = '../data/merged/merged_data.csv'

# Save the merged DataFrame to a CSV file
df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")

