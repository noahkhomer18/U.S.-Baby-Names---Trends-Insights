# U.S. Baby Names Analysis - Trends & Insights

A comprehensive analysis of U.S. baby names data to uncover naming trends, regional patterns, and unique characteristics across decades.

## 📊 Analysis Objectives

### Objective 1: Track Changes in Name Popularity
- Find the overall most popular girl and boy names and show how they have changed in popularity rankings over the years
- Identify the names with the biggest jumps in popularity from the first year of the dataset to the last year

### Objective 2: Compare Popularity Across Decades
- For each year, return the 3 most popular girl names and 3 most popular boy names
- For each decade, return the 3 most popular girl names and 3 most popular boy names

### Objective 3: Compare Popularity Across Regions
- Return the number of babies born in each of the six regions (NOTE: The state of MI should be in the Midwest region)
- Return the 3 most popular girl names and 3 most popular boy names within each region

### Objective 4: Explore Unique Names in the Dataset
- Find the 10 most popular androgynous names (names given to both females and males)
- Find the length of the shortest and longest names, and identify the most popular short names (those with the fewest characters) and long names (those with the most characters)
- Find the state with the highest percent of babies named "Chris"

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas, matplotlib, seaborn, numpy

### Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/noahkhomer18/U.S.-Baby-Names---Trends-Insights.git
   cd U.S.-Baby-Names---Trends-Insights
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements_direct.txt
   ```

3. **Run the analysis**
   ```bash
   python baby_names_analysis_simple.py
   ```

## 📁 Contents

- `names_data.csv` - Main dataset with U.S. baby names (State, Gender, Year, Name, Births)
- `baby_names_analysis_simple.py` - Complete analysis script that processes CSV directly
- `requirements_direct.txt` - Python dependencies
- `README.md` - This file
- `.gitignore` - Git ignore rules

## 🔍 Key Features

- **Direct CSV Processing** - No database setup required
- **Comprehensive Analysis** - Covers all 4 objectives completely
- **Regional Mapping** - Built-in U.S. state to region mapping
- **Immediate Results** - All analysis displayed in console
- **Clean Output** - Well-formatted results for easy reading

## 📈 Analysis Results

The script provides detailed analysis including:
- Overall most popular names by gender
- Names with biggest popularity jumps over time
- Top names by year and decade
- Regional birth distributions and top names
- Most popular androgynous names
- Name length analysis
- Chris popularity by state (answering the final project question)

## 🎯 Final Answer

**The state with the smallest percentage of babies named 'Chris' is West Virginia (WV) with 0.0018%**

## 💻 Technical Implementation

- **Data Processing**: Pandas for efficient CSV handling and data manipulation
- **Analysis**: GroupBy operations, ranking, and statistical calculations
- **Regional Logic**: Hardcoded state-to-region mapping ensuring MI is in Midwest
- **Performance**: Optimized for large datasets (2.2M+ records)

## 📊 Sample Output

The analysis provides comprehensive results including:
- Popularity trends over time
- Decade-by-decade comparisons
- Regional breakdowns
- Unique name characteristics
- Complete Chris analysis by state

Run the script to see all detailed results!
