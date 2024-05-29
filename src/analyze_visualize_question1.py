"""
Analyze the data to answer the project specific questions

Author: < Student Name >
"""
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('../data/merged/merged_data.csv')


# Average Total Stats: Calculate the average Total Stats for each Pokémon type. By looking at the average total stats, this will give me an idea of the overall strength of Pokémon belonging to each type.
avg_total = df.groupby('Type_1')['Total'].mean().sort_values(ascending = False)
# We can determine which type of defenders would be the strongest by looking at average defense stats.
avg_defense = df.groupby('Type_1')['Defense'].mean().sort_values(ascending = False)
# We can determine which type of fighters would be the strongest by looking at average attack stats.
avg_attack = df.groupby('Type_1')['Attack'].mean().sort_values(ascending = False)
# Create a new DataFrame to combine these averages
avg_stats = pd.DataFrame({
    'Average Total': avg_total,
    'Average Defense': avg_defense,
    'Average Attack': avg_attack
})

# Sort by one of the columns if needed, here I choose to sort by 'Average Total'
avg_stats = avg_stats.sort_values(by='Average Total', ascending=False)
print(avg_stats)

# Create the plot with the specified figure size
ax = avg_stats.plot(kind='bar', figsize=(15, 8))

# Setting the title and labels using the correct methods on the 'ax' object
ax.set_title('Average Stats by Type_1')
ax.set_xlabel('Type_1')
ax.set_ylabel('Values')

# Rotate the x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Show the plot
plt.show()





