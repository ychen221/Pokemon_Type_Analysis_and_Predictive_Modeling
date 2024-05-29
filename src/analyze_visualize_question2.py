import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('../data/merged/merged_data.csv')

# create a popularity subdataset
pop_df = df[['Name','capture_rate', 'forms_switchable', 'Total', 'is_legendary', 'Counts', 'Body_Style','is_mythical', 'hasMegaEvolution' ]]

# Scatter plot for Capture Rate vs. Counts
plt.figure(figsize=(10, 6))
sns.scatterplot(x='capture_rate', y='Counts', data=pop_df)
plt.title('Popularity vs. Capture Rate')
plt.xlabel('Capture Rate')
plt.ylabel('Popularity (Counts)')
plt.show()

# Scatter plot for Total Stats vs. Counts
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total', y='Counts', data=pop_df)
plt.title('Popularity vs. Total Stats')
plt.xlabel('Total Stats')
plt.ylabel('Popularity (Counts)')
plt.show()

# Bar plot for Forms Switchable vs. Counts
plt.figure(figsize=(6, 6))
sns.barplot(x='forms_switchable', y='Counts', data=pop_df, estimator=np.mean, errorbar=None)
plt.title('Average Popularity (Counts) vs. Forms Switchable')
plt.xlabel('Forms Switchable ((0 = No, 1 = Yes))')
plt.ylabel('Average Popularity (Counts)')
plt.show()

# Bar plot for Is Legendary vs. Counts

plt.figure(figsize=(6, 6))
sns.barplot(x='is_legendary', y='Counts', data=pop_df, estimator=np.mean, errorbar=None)
plt.title('Average Popularity (Counts) by Legendary Status')
plt.xlabel('Is Legendary (0 = No, 1 = Yes)')
plt.ylabel('Average Popularity (Counts)')
plt.show()

# Bar plot for Is mythical vs. Counts
plt.figure(figsize=(6, 6))
sns.barplot(x='is_mythical', y='Counts', data=pop_df, estimator=np.mean, errorbar=None)
plt.title('Average Popularity (Counts) by Mythical Status')
plt.xlabel('Is Mythical (0 = No, 1 = Yes)')
plt.ylabel('Average Popularity (Counts)')
plt.show()

# Bar plot for mega-evolution vs. Counts
plt.figure(figsize=(6, 6))
sns.barplot(x='hasMegaEvolution', y='Counts', data=pop_df, estimator=np.mean, errorbar=None)
plt.title('Average Popularity (Counts) by hasMegaEvolution Status')
plt.xlabel('hasMegaEvolution (0 = No, 1 = Yes)')
plt.ylabel('Average Popularity (Counts)')
plt.show()

# Scatter plot for Body style vs. Counts
# Calculate mean counts for each body style
ordered_body_styles = pop_df.groupby('Body_Style')['Counts'].sum().sort_values(ascending=False)
# Converting the Series to a DataFrame and renaming columns
ordered_body_styles = ordered_body_styles.reset_index()
ordered_body_styles.columns = ['Body_Style', 'Total_Counts']
ordered_body_styles

plt.figure(figsize=(15, 6))
sns.barplot(x='Body_Style', y='Total_Counts', data=ordered_body_styles)
plt.title('Popularity vs. Body Style ')
plt.xlabel('Body Style')
plt.ylabel('Popularity (Counts)')
plt.xticks(rotation=45)  # Rotate x labels for better readability

plt.show()
print(ordered_body_styles)
