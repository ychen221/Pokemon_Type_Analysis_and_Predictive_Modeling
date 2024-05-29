"""
Clean the data, transform the data and store the files in the data/processed folder

Author: < Student Name>
"""
import pandas as pd

# Load the dataset
source2_df = pd.read_csv('../data/raw/source2_scraped_data.csv')

#clean source2_df
#handle missing value
#inspect if there is missing value
missing_values = source2_df.isnull().sum()
# Select numeric columns and replace missing values with the mean of each column
source2_df.select_dtypes(include=['int64', 'float64']).apply(lambda x: x.fillna(x.mean()), axis=0).pipe(source2_df.update)
# inspect the missing value after dealing with it
missing_values = source2_df.isnull().sum()
# drop order and id column 
cleaned_source2_df = source2_df.drop(['order','id'], axis=1)
# Define the output path for the cleaned CSV file
output_path = '../data/processed/cleaned_source2_scraped_data.csv'

# Save the cleaned DataFrame to a CSV file
cleaned_source2_df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")
