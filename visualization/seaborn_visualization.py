import matplotlib
# This allows us to save the plot as an image file
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
# Import the pre-calculated bubble positions from our external data file
from my_data import coordinates 

# Created a sorted list of unique country names from the data (index 5 is Country)
unique_countries = sorted(list(set([item[5] for item in coordinates]))) 

# Generates a distinct color palette (HUSL) with one color per country
palette = sns.color_palette("husl", len(unique_countries))

# Creates a lookup dictionary: {'CountryName': 'Color'}
color_map = dict(zip(unique_countries, palette))

plt.figure(figsize=(14, 12))
ax = plt.gca() # Get Current Axis: We need this handle to manually add shapes

# Unpack each row of data into readable variables
for (x, y, r, city_name, score, country) in coordinates:
    color = color_map[country]
    
    # Create the Circle object with thee color 'color' and black border then add it to the plot
    circle = plt.Circle((x, y), r, color=color, ec='black')
    ax.add_patch(circle)
    
    # Adds the text label in the center with a dynamic font size in bold black
    plt.text(x, y, f"{city_name}\n{score:.0f}", ha='center', va='center', 
             fontsize=max(8, r/3), weight='bold', color='black')

#The custom Legend: here scince we used 'add_patch' the legend isn't auto generated
# We create "fake" dots  (Line2D objects with no length) to populate the legend key.
legend_elements = [Line2D([0], [0], marker='o', color='w', label=c, 
                          markerfacecolor=color_map[c], markersize=12, mec='black') 
                   for c in unique_countries]

# bbox_to_anchor=(1, 0.5): Anchors the legend to the right edge of the chart 
#ncol= number of columns 
ax.legend(handles=legend_elements, title="Country", loc="center left", bbox_to_anchor=(1, 0.5), ncol=3)

plt.axis('scaled') # Force 1:1 aspect ratio so circles stay round
plt.axis('off') # Hide the axis
limit = 200  #zoom limits 
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)
plt.title('Hidden Gem Index: 30 Cities', fontsize=16, weight='bold')

plt.tight_layout() #to prevent text cutoff
plt.savefig('Hidden Gem Index.png') # Save directly to file
