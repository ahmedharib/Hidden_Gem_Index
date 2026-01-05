"""
This module processes Numbeo data to calculate a 'Hidden Gem' score for various
cities/countries. It cleans the raw JSON data and exports a final JSON with scores.
"""
import pandas as pd

# Load the messy data
df = pd.read_json(r'data_cleaning\numbeo_data.json')

# Combine rows with the same city name
# This "collapses" the 7 rows into 1
df_clean = df.groupby('country').first().reset_index()

# Drop the rows with missing values
df_clean.dropna(inplace=True)

# Re-number the rows from 0 to the end
# drop = True means "don't turn the old messy index into a new column"
df_clean.reset_index(drop=True, inplace=True)

def calculate_score(row):
    """
    Calculates the 'Hidden Gem' score based on various quality of life metrics.
    """
    # Short names to make the formula easier to read
    # Renamed variables to satisfy Pylint C0103 (must be > 2 chars)
    purchasing_power = row['purchasing_power_index']
    safety = row['safety_index']
    health_care = row['health_care_index']
    cost_living = row['cost_of_living_plus_rent_index']
    prop_ratio = row['property_price_to_income_ratio']
    traffic = row['traffic_index']
    pollution = row['pollution_index']

    # The formula calculation
    # Wrapped in parentheses to allow multi-line formatting (Fixes C0301)
    score = (100 + (purchasing_power / 2.5) + (safety / 2.0) +
             (health_care / 2.5) - (cost_living / 5.0) -
             (prop_ratio * 1.5) - (traffic / 2.0) -
             (2 * pollution / 3.0))

    # Python's built-in max (keeps it 0 or higher) than rounds the value
    final_result = round(max(0, score), 1)

    return final_result

# adds 'final_score' column to df using calculate_score function
df_clean['final_score'] = df_clean.apply(calculate_score, axis=1)

# prints dataframe as rows and columns
# print(df_clean.to_string())

# converts data frame to json file
df_clean.to_json('cleaned_numbeo_data.json', index=False)
