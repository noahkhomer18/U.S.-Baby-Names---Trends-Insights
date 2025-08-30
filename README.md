# U.S. Baby Names Analysis - Trends & Insights

A comprehensive data analysis project exploring U.S. baby naming patterns across decades, regions, and unique characteristics using Python and data science techniques.

## Overview

This project analyzes a comprehensive dataset of U.S. baby names (2.2M+ records) to uncover naming trends, regional patterns, and demographic insights. The analysis covers data from multiple decades and all 50 states, providing insights into how naming preferences have evolved over time and vary across different regions of the country.

**Dataset**: Historical U.S. baby names data including State, Gender, Year, Name, and Births (1980-2010s)

## Features / What I Did

### Data Analysis & Processing
- **Comprehensive Data Cleaning**: Handled CSV files without headers, created proper column mappings
- **Regional Classification System**: Built custom U.S. state-to-region mapping ensuring accurate geographic categorization
- **Time-Series Analysis**: Analyzed naming trends across decades and individual years
- **Statistical Ranking**: Implemented ranking algorithms to identify top names by various criteria

### Key Analytical Insights
- **Popularity Tracking**: Identified overall most popular names (Jessica for girls, Michael for boys) and their yearly trends
- **Trend Analysis**: Discovered names with biggest popularity jumps (Isabella: +22,266 births from first to last year)
- **Decade Comparisons**: Analyzed top 3 names by gender for each decade (1980s, 1990s, 2000s)
- **Regional Patterns**: Mapped birth distributions and top names across 6 U.S. regions
- **Unique Name Characteristics**: Identified most popular androgynous names and analyzed name length distributions

### Final Project Question
**Solved**: "Which state had the smallest percentage of babies named 'Chris'?"
**Answer**: West Virginia (WV) with 0.0018% - determined through comprehensive percentage calculations across all states

## Tech Stack

- **Python 3.7+** - Core programming language
- **Pandas** - Data manipulation, grouping, and statistical analysis
- **NumPy** - Numerical operations and array handling
- **Data Analysis Techniques**:
  - GroupBy operations and aggregations
  - Window functions and ranking algorithms
  - Pivot tables and data reshaping
  - Statistical calculations and percentage analysis

## What I Learned

This project significantly enhanced my **data science and Python programming skills**. I gained hands-on experience with large-scale data processing (2.2M+ records), learned advanced Pandas operations including complex GroupBy operations and pivot tables, and developed strong analytical thinking for uncovering patterns in demographic data. The project taught me how to handle real-world data challenges like missing headers, create efficient data processing pipelines, and present complex findings in clear, actionable insights.

## How It Works

### Data Flow
1. **Input**: Loads CSV file with baby names data (State, Gender, Year, Name, Births)
2. **Processing**: 
   - Creates regional mapping for geographic analysis
   - Performs statistical aggregations by various dimensions
   - Implements ranking algorithms for popularity analysis
   - Calculates percentage distributions and trend changes
3. **Output**: Comprehensive analysis results displayed in console including:
   - Overall popularity rankings
   - Decade-by-decade comparisons
   - Regional birth distributions
   - Unique name characteristics
   - Final Chris analysis with state rankings

### Analysis Pipeline
- **Objective 1**: Popularity tracking and trend analysis
- **Objective 2**: Yearly and decade-based comparisons
- **Objective 3**: Regional pattern analysis
- **Objective 4**: Unique name exploration and Chris percentage analysis

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/noahkhomer18/U.S.-Baby-Names---Trends-Insights.git
cd U.S.-Baby-Names---Trends-Insights

# Install required packages
pip install pandas numpy

# Run the analysis
python baby_names_analysis_simple.py
```

### Expected Output
The script will display comprehensive analysis results including:
- Overall most popular names by gender
- Names with biggest popularity changes
- Top names by decade and region
- Most popular androgynous names
- Complete Chris analysis by state

## Project Structure

```
├── names_data.csv                    # Main dataset (2.2M+ records)
├── baby_names_analysis_simple.py    # Complete analysis script
├── requirements_direct.txt           # Python dependencies
├── popularity_jumps.png             # Visualization of popularity changes
├── popularity_trends.png            # Visualization of trends over time
└── README.md                        # This file
```

## Key Results

- **Most Popular Names**: Jessica (F: 863K births), Michael (M: 1.38M births)
- **Biggest Trend**: Isabella's popularity increased by 22,266 births
- **Regional Leader**: South region with 34.2M total births
- **Final Answer**: WV has smallest Chris percentage at 0.0018%

This project demonstrates strong data analysis skills, Python programming proficiency, and the ability to extract meaningful insights from large, complex datasets.
