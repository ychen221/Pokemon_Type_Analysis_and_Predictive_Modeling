# DSCI510 Final Project

## 1. Objective
This project aims to investigate several aspects of player engagement and Pokémon game dynamics. First, it looks at a Pokémon's innate traits to determine which of them are capable of Mega Evolution. Secondly, the research will perform a statistical analysis to compare the average total base stats of Pokémon across different types, identifying any significant trends or differences. Finally, it will look into the connection between Pokémon's in-game traits and statistics and their popularity as determined by mentions on the Pokémon Fandom forum. This thorough approach will provide light on how these variables affect player engagement and game balance.


## 2. Install Dependencies
pip install -r requirements.txt


## 3. Download the Data Source and save it in the raw folder
1. Pokemon_fandom_data_source1(scraper1)
- To download and print All Data to the Console:
The command below will execute scraper1 in its default mode, where it prints all the data directly to your console.
Go to the src directory, and the command to execute is: python scraper1.py

- To Save the Scraped Data to a CSV File and save it in the raw folder:
Go to the src directory, and the command to execute is: python scraper1.py --save ../data/raw/source1_scraped_data.csv


2. Pokemon_attributes_API_source2(scraper2)
- To download and print All Data to the Console:
Run the script without any arguments if you want to print all the data to the console. Every Pokémon species' worth of data will be retrieved, then printed to the console.
Go to the src directory, and the command to execute is: python scraper2.py

- To Save the Scraped Data to a CSV File and save it in the raw folder:
To save the information to a CSV file, use the --save option and a file path.
Go to the src directory, and the command to execute is: python scraper2.py --save ../data/raw/source2_scraped_data.csv


3. Pokemon Stats from Kaggle: 
I have already downloaded it and save it in the raw folder

## 4. Clean the data 
1. My source1 does not need to be cleaned, so I directly put it in the processed folder. 

2. The clean_data2.py script automates data cleaning by loading data from ../data/raw/source2_scraped_data.csv, handling missing values in numeric columns by replacing them with column means, and dropping unnecessary 'order' and 'id' columns. The cleaned data is then saved to ../data/processed/cleaned_source2_scraped_data.csv without including row indices. To run the script and perform these operations, go to the src directory, and the command to execute is : python clean_data2.py 

3. The script clean_data3.py loads data from ../data/raw/source3_static_data.csv, checks for missing values, and removes columns ('Type_2', 'Egg_Group_2', 'Number') with excessive missing data or redundancy. It replaces missing values in the 'Pr_Male' column with the mean, then saves the cleaned dataset to ../data/processed/cleaned_source3_scraped_data.csv. To execute the script, go to the src directory, and use the command: python clean_data3.py


## 5. Integrate the data (integrate_data.py)
The script merges data from cleaned_source1_scraped_data.csv, cleaned_source2_scraped_data.csv, and cleaned_source3_static_data.csv using pandas. This integration focuses on matching entries by the 'Name' column, initially merging source2_df and source3_df with an inner join, and then merging the resulting DataFrame with source1_df using an outer join.The final output integrated dataset is called 'df', and then I converted it to a csv file and stored it in the merged folder
To execute the script, go to the src directory, and use the command: python integrate_data.py

## 6. analyze the data and create visuailzation to answer the questions
1. analyze_visualize_question1.py: Basically this script answer question 1, and it performs the tasks:
- Calculates the average total stats for each Pokémon type.
- Identifies types of Pokemons that are the strongest defenders based on average defense stats.
- Identifies types of Pokemons that are the strongest fighters based on average attack stats.
- Sorts these averages by average total stats and merges them into a new DataFrame.
- The script also creates a bar chart that visualizes the average stats for each Pokémon type, including total stats, defense, and attack. 
- To run the analysis, go to the src directory and execute it by using the command: python analyze_visualize_question1.py

2. analyze_visualize_question2.py:Includes the code needed to create visuals that investigate the relationship between certain Pokémon attributes and popularity, as determined by mentions of the Pokémon in Pokemon fandom forum.The script generates the following visualizations:
- Capture Rate vs. Popularity:
It analyzes how the capture rate of Pokémon correlates with their popularity.
- Total Stats vs. Popularity:
It shows the relationship between the total stats of Pokémon and their popularity counts.
- Average Popularity by Forms Switchable:
Bar plot indicates the average popularity for Pokémon that can switch forms versus those that cannot.
- Average Popularity by Legendary Status:
Bar plot compares the popularity of legendary versus non-legendary Pokémon.
- Popularity vs. Body Style:
Bar plot displaying popularity across different Pokémon body styles, sorted by total counts.
- To run the analysis, go to the src directory and execute it by using the command: python analyze_visualize_question2.py


## 7. Build a machine learning model on predicting Pokemon Mega-Evolution:
1. building_predictive_model_question3.py: This script specifically answer the question 3, and it contains the following execution:
- Data preprocessing: 
It eliminates all categorical variables, and the dataset's 'capture_rate' attribute.Also it divides the input into two variables: features (X) and target variable (y), where the target is the presence of Mega Evolution in a Pokémon.
- Model Training:
It divides the data into training and testing sets for the model, and uses 100 trees to train a Random Forest classifier.
- Model Evaluation: 
Print the accuracy and a classification report including precision, recall, and F1-score which are used to assess the model's performance on a test set.
- To run the analysis, go to the project directory (src) and execute it by using the command: python building_predictive_model_question3.py




## Acknowledgements
https://www.kaggle.com/datasets/alopez247/pokemon
https://pokeapi.co/docs/v2
https://pokemon.fandom.com/f?catId=74


