import pandas as pd

# Load the messy data
df = pd.read_json('numbeo_data.json')

# Combine rows with the same city name
# This "collapses" the 7 rows into 1
df_clean = df.groupby('country').first().reset_index()

# Drop the rows with missing values
df_clean.dropna(inplace = True)

# Re-number the rows from 0 to the end
# drop = True means "don't turn the old messy index into a new column"
df_clean.reset_index(drop = True, inplace = True)

# Applying the formula
def calculate_score(row):
    # Short names to make the formula easier to read
    pp = row['purchasing_power_index']
    safe = row['safety_index']
    hc = row['health_care_index']
    col = row['cost_of_living_plus_rent_index']
    prop = row['property_price_to_income_ratio']
    traffic = row['traffic_index']
    poll = row['pollution_index']

    # The formula calculation
    score = 100 + (pp / 2.5) + (safe / 2.0) + (hc / 2.5) - (col / 5.0) - (prop * 1.5) - (traffic / 2.0) - (2 * poll / 3.0)
    
    # Python's built-in max (keeps it 0 or higher) than rounds the value
    final_result = round(max(0, score), 1)

    return final_result

# adds 'final_score' column to df using calculate_score function
df_clean['final_score'] = df_clean.apply(calculate_score, axis = 1)

# prints dataframe as rows and columns
# print(df_clean.to_string())

# converts data frame to json file
df_clean.to_json('cleaned_numbeo_data.json', index=False)

