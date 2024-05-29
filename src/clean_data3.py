import pandas as pd
# source3_df cleaning
#inspect if there is missing value
source3_df = pd.read_csv('../data/raw/source3_static_data.csv')

missing_values2 = source3_df.isnull().sum()
# drop Type_2 and Egg_Group_2 since they have to many missing values
# drop number 
# Specify the columns to be dropped
drop_columns = ['Type_2', 'Egg_Group_2', 'Number']

# Drop the specified columns from source3_df
source3_df.drop(drop_columns, axis=1, inplace=True)

# Pr_male missing values replace with mean
# Calculate the mean of the Pr_Male column
pr_male_mean = source3_df['Pr_Male'].mean()

# Replace missing values in the Pr_Male column with the calculated mean
source3_df['Pr_Male'].fillna(pr_male_mean, inplace=True)
cleaned_source3_df = source3_df
# Display the DataFrame 
cleaned_source3_df

# Define the output path for the cleaned CSV file
output_path = '../data/processed/cleaned_source3_static_data.csv'

# Save the cleaned DataFrame to a CSV file
cleaned_source3_df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")
