import argparse
import requests
import pandas as pd

def get_pokemon_species_data(pokemon_species_id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_species_id_or_name}/"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_species_data = response.json()
        desired_fields = ['base_happiness', 'capture_rate', 'forms_switchable', 'gender_rate', 
                          'has_gender_differences', 'hatch_counter', 'id', 'is_baby', 
                          'is_legendary', 'is_mythical', 'name', 'order']
        extracted_data = {field: pokemon_species_data[field] for field in desired_fields if field in pokemon_species_data}
        return extracted_data
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None

def get_all_pokemon_species_names():
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    all_species_names = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            species_names = [result['name'] for result in data['results']]
            all_species_names.extend(species_names)
            url = data.get('next')
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            return None
    return all_species_names


def fetch_and_consolidate_pokemon_data(limit=None):
    species_names = get_all_pokemon_species_names()
    if limit:
        species_names = species_names[:limit]

    detailed_data = []
    for name in species_names:
        data = get_pokemon_species_data(name)
        if data:
            # Ensure the 'name' field is included and set it explicitly if necessary
            data['name'] = name  # This line ensures each entry has a 'name' key with the Pokémon's name
            detailed_data.append(data)
    
    # Create DataFrame from the list of dictionaries
    df = pd.DataFrame(detailed_data)

    
    if 'name' in df.columns:
        df.rename(columns={'name': 'Name'}, inplace=True)  # Rename 'name' column to 'Name'
        # Reorder DataFrame to have 'Name' as the first column
        cols = ['Name'] + [col for col in df.columns if col != 'Name']
        df = df[cols]

    return df


def save_data(df, filepath):
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Pokémon Species Data Scraper")
    parser.add_argument('--scrape', type=int, help="Scrape only the first N entries of the dataset")
    parser.add_argument('--save', type=str, help="Path to save the scraped data")
    args = parser.parse_args()

    if args.scrape is not None:
        pokemon_df = fetch_and_consolidate_pokemon_data(limit=args.scrape)
    else:
        pokemon_df = fetch_and_consolidate_pokemon_data()

    if args.save:
        save_data(pokemon_df, args.save)
    else:
        print(pokemon_df)

if __name__ == "__main__":
    main()
