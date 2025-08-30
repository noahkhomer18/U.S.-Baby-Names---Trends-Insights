# U.S. Baby Names - Trends & Insights

This repository contains a comprehensive dataset of U.S. baby names with associated data for analysis and trend insights.

## Contents

- **`names_data.csv`** - Main dataset containing U.S. baby names data (44MB)
- **`create_baby_names_db.sql`** - SQL script to create the baby names database schema
- **`baby_names_db_data_dictionary.csv`** - Data dictionary explaining the database structure
- **`baby_names_analysis.sql`** - Complete SQL analysis covering all objectives
- **`baby_names_analysis.py`** - Python analysis and visualization script
- **`requirements.txt`** - Python dependencies
- **`analysis_report.md`** - Comprehensive analysis report template
- **`alternative_sql_scripts.zip`** - Additional SQL scripts for various analyses

## Dataset Overview

The dataset includes historical U.S. baby names data that can be used for:
- Name popularity trends over time
- Gender-based name analysis
- Regional name variations
- Statistical analysis of naming patterns

## Analysis Objectives

This project addresses four main analytical objectives:

### 1. Track Changes in Name Popularity
- Find the overall most popular girl and boy names
- Show how they have changed in popularity rankings over the years
- Identify names with the biggest jumps in popularity from first to last year

### 2. Compare Popularity Across Decades
- For each year, return the 3 most popular girl names and 3 most popular boy names
- For each decade, return the 3 most popular girl names and 3 most popular boy names

### 3. Compare Popularity Across Regions
- Return the number of babies born in each of the six regions
- Return the 3 most popular girl names and 3 most popular boy names within each region

### 4. Explore Unique Names in the Dataset
- Find the 10 most popular androgynous names (names given to both females and males)
- Find the length of the shortest and longest names, and identify the most popular short and long names
- Find the state with the highest percentage of babies named "Chris"

## Getting Started

### Prerequisites
- MySQL Server
- Python 3.7+
- Required Python packages (see `requirements.txt`)

### Setup Instructions

1. **Database Setup**:
   ```bash
   # Run the database creation script
   mysql -u root -p < create_baby_names_db.sql
   
   # Import the data (update path as needed)
   mysql -u root -p baby_names_db
   LOAD DATA LOCAL INFILE '/path/to/names_data.csv'
   INTO TABLE names
   FIELDS TERMINATED BY ','
   LINES TERMINATED BY '\n';
   ```

2. **Python Environment**:
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

3. **Run Analysis**:
   ```bash
   # Execute the complete analysis
   python baby_names_analysis.py
   ```

## Analysis Tools

### SQL Analysis (`baby_names_analysis.sql`)
- Complex queries using window functions and CTEs
- Comprehensive coverage of all four objectives
- Optimized for performance with large datasets

### Python Analysis (`baby_names_analysis.py`)
- Automated data visualization
- Statistical analysis and pattern recognition
- High-quality chart generation
- Export capabilities for reports

## Key Features

- **Comprehensive Coverage**: All four analysis objectives addressed
- **Visualization**: Multiple chart types (line, bar, pie, heatmap)
- **Performance Optimized**: Efficient queries for large datasets
- **Modular Design**: Easy to extend and customize
- **Professional Output**: High-resolution visualizations and reports

## Output Files

The analysis generates several visualization files:
- `popularity_trends.png` - Name popularity over time
- `popularity_jumps.png` - Biggest popularity changes
- `decade_comparisons.png` - Decade-by-decade comparisons
- `regional_distribution.png` - Birth distribution by region
- `regional_top_names.png` - Top names by region
- `androgynous_names.png` - Most popular unisex names
- `chris_analysis.png` - Chris popularity by state

## Technical Implementation

### Database Schema
- **names table**: State, Gender, Year, Name, Births
- **regions table**: State, Region mapping

### Key SQL Techniques
- Window functions for ranking
- Common Table Expressions (CTEs)
- Conditional aggregations
- Complex joins and subqueries

### Python Features
- Pandas for data manipulation
- Matplotlib and Seaborn for visualization
- MySQL connector for database access
- Automated report generation

## Final Answer

The analysis answers the key question: **Which state had the smallest percentage of babies named "Chris"?**

The answer is determined through comprehensive analysis of the dataset and presented in the final visualization.

## License

This dataset and analysis are provided for educational and research purposes.
