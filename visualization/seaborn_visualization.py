import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from matplotlib.lines import Line2D
from my_data import coordinates 

unique_countries = sorted(list(set([item[5] for item in coordinates])))
palette = sns.color_palette("husl", len(unique_countries))
color_map = dict(zip(unique_countries, palette))

plt.figure(figsize=(14, 12))
ax = plt.gca()

for (x, y, r, city_name, score, country) in coordinates:
    color = color_map[country]
    
    circle = plt.Circle((x, y), r, color=color, ec='black')
    ax.add_patch(circle)
    
    plt.text(x, y, f"{city_name}\n{score:.0f}", ha='center', va='center', 
             fontsize=max(8, r/3), weight='bold', color='black')

legend_elements = [Line2D([0], [0], marker='o', color='w', label=c, 
                          markerfacecolor=color_map[c], markersize=12, mec='black') #c->country name
                   for c in unique_countries]

ax.legend(handles=legend_elements, title="Country", loc="center left", bbox_to_anchor=(1, 0.5), ncol=3)

plt.axis('scaled')
plt.axis('off')
limit = 200 
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)
plt.title('Hidden Gem Index: 30 Cities', fontsize=16, weight='bold')

plt.tight_layout()
plt.savefig('visualization.png')