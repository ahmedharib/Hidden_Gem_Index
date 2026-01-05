# Hidden Gem Index Analyzer

This project scrapes global quality-of-life data, processes it to identify "undervalued" cities (Hidden Gems), and visualizes the top results as a packed bubble chart.

## 📂 Project Structure

* **`index_spider.py`**: A Scrapy spider that crawls *Numbeo.com* to fetch raw data for various indices (Cost of Living, Safety, Health Care, Traffic, Pollution, etc.).
* **`data_cleaning_script.py`**: A Pandas script that merges the raw data, cleans it (handling missing values), and calculates a custom "Hidden Gem Score" for each city.
* **`seaborn_visualization.py`**: Generates a polished bubble chart visualization of the top 30 cities using Matplotlib and Seaborn.
* **`final_data_version.py`**: Contains the pre-calculated coordinates for the circle packing visualization.

## 🚀 Installation

1.  **Clone or download** this repository.
2.  **Install the required Python packages**:
```bash
    pip install -r requirements.txt
```

## ⚙️ How to Run

### 1. Scrape the Data
Run the Scrapy spider to fetch the latest data from Numbeo. This will generate a JSON file with raw data.
```bash
scrapy runspider index_spider.py -o numbeo_data.json
```