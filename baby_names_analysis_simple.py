import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up the plotting style
plt.style.use('default')
sns.set_palette("husl")

class BabyNamesAnalyzerSimple:
    def __init__(self, csv_file='names_data.csv'):
        """Initialize the analyzer with CSV file"""
        self.csv_file = csv_file
        self.names_df = None
        self.regions_df = None
        
    def load_data(self):
        """Load data from CSV files"""
        try:
            print("Loading baby names data...")
            # Load CSV without headers and assign proper column names
            self.names_df = pd.read_csv(self.csv_file, header=None, 
                                      names=['State', 'Gender', 'Year', 'Name', 'Births'])
            print(f"Loaded {len(self.names_df)} records")
            
            # Create regions mapping (since we don't have the regions table)
            self.create_regions_mapping()
            
            print("Data loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def create_regions_mapping(self):
        """Create regions mapping for U.S. states"""
        regions_data = {
            'AL': 'South', 'AK': 'Pacific', 'AZ': 'Mountain', 'AR': 'South', 'CA': 'Pacific',
            'CO': 'Mountain', 'CT': 'New_England', 'DC': 'Mid_Atlantic', 'DE': 'South', 'FL': 'South',
            'GA': 'South', 'HI': 'Pacific', 'ID': 'Mountain', 'IL': 'Midwest', 'IN': 'Midwest',
            'IA': 'Midwest', 'KS': 'Midwest', 'KY': 'South', 'LA': 'South', 'ME': 'New_England',
            'MD': 'South', 'MA': 'New_England', 'MI': 'Midwest', 'MN': 'Midwest', 'MS': 'South',
            'MO': 'Midwest', 'MT': 'Mountain', 'NE': 'Midwest', 'NV': 'Mountain', 'NH': 'New_England',
            'NJ': 'Mid_Atlantic', 'NM': 'Mountain', 'NY': 'Mid_Atlantic', 'NC': 'South', 'ND': 'Midwest',
            'OH': 'Midwest', 'OK': 'South', 'OR': 'Pacific', 'PA': 'Mid_Atlantic', 'RI': 'New_England',
            'SC': 'South', 'SD': 'Midwest', 'TN': 'South', 'TX': 'South', 'UT': 'Mountain',
            'VT': 'New_England', 'VA': 'South', 'WA': 'Pacific', 'WV': 'South', 'WI': 'Midwest', 'WY': 'Mountain'
        }
        
        self.regions_df = pd.DataFrame(list(regions_data.items()), columns=['State', 'Region'])
        
        # Merge regions with names data
        self.names_df = self.names_df.merge(self.regions_df, on='State', how='left')
    
    def analyze_popularity_changes(self):
        """Objective 1: Track changes in name popularity"""
        print("\n" + "="*60)
        print("OBJECTIVE 1: TRACKING NAME POPULARITY CHANGES")
        print("="*60)
        
        # 1.1 Overall most popular names and their yearly trends
        print("\n1.1 Overall Most Popular Names:")
        
        # Get overall most popular names
        overall_popular = self.names_df.groupby(['Name', 'Gender'])['Births'].sum().reset_index()
        overall_popular = overall_popular.sort_values('Births', ascending=False)
        
        top_girl = overall_popular[overall_popular['Gender'] == 'F'].iloc[0]
        top_boy = overall_popular[overall_popular['Gender'] == 'M'].iloc[0]
        
        print(f"Girls: {top_girl['Name']} - {top_girl['Births']:,} total births")
        print(f"Boys: {top_boy['Name']} - {top_boy['Births']:,} total births")
        
        # Get yearly trends for top names
        top_names_data = self.names_df[
            ((self.names_df['Name'] == top_girl['Name']) & (self.names_df['Gender'] == 'F')) |
            ((self.names_df['Name'] == top_boy['Name']) & (self.names_df['Gender'] == 'M'))
        ]
        
        yearly_trends = top_names_data.groupby(['Year', 'Name', 'Gender'])['Births'].sum().reset_index()
        
        print("\nYearly Trends (Sample):")
        print(yearly_trends.head(10))
        
        # 1.2 Names with biggest popularity jumps
        print("\n1.2 Names with Biggest Popularity Jumps:")
        
        # Get first and last years
        first_year = self.names_df['Year'].min()
        last_year = self.names_df['Year'].max()
        
        # Calculate popularity changes
        first_year_data = self.names_df[self.names_df['Year'] == first_year].groupby(['Name', 'Gender'])['Births'].sum().reset_index()
        last_year_data = self.names_df[self.names_df['Year'] == last_year].groupby(['Name', 'Gender'])['Births'].sum().reset_index()
        
        # Merge and calculate changes
        popularity_changes = first_year_data.merge(last_year_data, on=['Name', 'Gender'], suffixes=('_first', '_last'))
        popularity_changes['popularity_change'] = popularity_changes['Births_last'] - popularity_changes['Births_first']
        
        # Filter for names that existed in both years
        popularity_changes = popularity_changes[
            (popularity_changes['Births_first'] > 0) & (popularity_changes['Births_last'] > 0)
        ]
        
        top_changes = popularity_changes.nlargest(10, 'popularity_change')
        print(top_changes[['Name', 'Gender', 'Births_first', 'Births_last', 'popularity_change']])
    
    def analyze_decade_comparisons(self):
        """Objective 2: Compare popularity across decades"""
        print("\n" + "="*60)
        print("OBJECTIVE 2: DECADE COMPARISONS")
        print("="*60)
        
        # 2.1 Top 3 names by year
        print("\n2.1 Top 3 Names by Year (Sample):")
        
        yearly_rankings = self.names_df.groupby(['Year', 'Name', 'Gender'])['Births'].sum().reset_index()
        yearly_rankings['rank_in_year'] = yearly_rankings.groupby(['Year', 'Gender'])['Births'].rank(method='dense', ascending=False)
        
        top_3_yearly = yearly_rankings[yearly_rankings['rank_in_year'] <= 3].sort_values(['Year', 'Gender', 'rank_in_year'])
        print(top_3_yearly.head(15))
        
        # 2.2 Top 3 names by decade
        print("\n2.2 Top 3 Names by Decade:")
        
        # Create decade column
        self.names_df['decade'] = (self.names_df['Year'] // 10) * 10
        
        decade_data = self.names_df.groupby(['decade', 'Name', 'Gender'])['Births'].sum().reset_index()
        decade_data['rank_in_decade'] = decade_data.groupby(['decade', 'Gender'])['Births'].rank(method='dense', ascending=False)
        
        top_3_decade = decade_data[decade_data['rank_in_decade'] <= 3].sort_values(['decade', 'Gender', 'rank_in_decade'])
        print(top_3_decade)
    
    def analyze_regional_patterns(self):
        """Objective 3: Compare popularity across regions"""
        print("\n" + "="*60)
        print("OBJECTIVE 3: REGIONAL ANALYSIS")
        print("="*60)
        
        # 3.1 Babies born by region
        print("\n3.1 Number of Babies Born by Region:")
        
        regional_births = self.names_df.groupby('Region')['Births'].sum().reset_index()
        regional_births = regional_births.sort_values('Births', ascending=False)
        print(regional_births)
        
        # 3.2 Top names by region
        print("\n3.2 Top 3 Names by Region:")
        
        regional_rankings = self.names_df.groupby(['Region', 'Name', 'Gender'])['Births'].sum().reset_index()
        regional_rankings['rank_in_region'] = regional_rankings.groupby(['Region', 'Gender'])['Births'].rank(method='dense', ascending=False)
        
        top_3_regional = regional_rankings[regional_rankings['rank_in_region'] <= 3].sort_values(['Region', 'Gender', 'rank_in_region'])
        print(top_3_regional)
    
    def analyze_unique_names(self):
        """Objective 4: Explore unique names in the dataset"""
        print("\n" + "="*60)
        print("OBJECTIVE 4: UNIQUE NAMES ANALYSIS")
        print("="*60)
        
        # 4.1 Most popular androgynous names
        print("\n4.1 Most Popular Androgynous Names:")
        
        androgynous = self.names_df.groupby(['Name', 'Gender'])['Births'].sum().reset_index()
        androgynous_pivot = androgynous.pivot(index='Name', columns='Gender', values='Births').fillna(0)
        
        # Names given to both genders
        androgynous_names = androgynous_pivot[(androgynous_pivot['F'] > 0) & (androgynous_pivot['M'] > 0)]
        androgynous_names['total_births'] = androgynous_names['F'] + androgynous_names['M']
        
        top_androgynous = androgynous_names.nlargest(10, 'total_births')[['F', 'M', 'total_births']]
        print(top_androgynous)
        
        # 4.2 Name length analysis
        print("\n4.2 Name Length Analysis:")
        
        name_lengths = self.names_df.groupby('Name')['Births'].sum().reset_index()
        name_lengths['name_length'] = name_lengths['Name'].str.len()
        
        shortest_length = name_lengths['name_length'].min()
        longest_length = name_lengths['name_length'].max()
        
        shortest_names = name_lengths[name_lengths['name_length'] == shortest_length].nlargest(5, 'Births')
        longest_names = name_lengths[name_lengths['name_length'] == longest_length].nlargest(5, 'Births')
        
        print(f"Shortest names ({shortest_length} characters):")
        print(shortest_names[['Name', 'name_length', 'Births']])
        
        print(f"\nLongest names ({longest_length} characters):")
        print(longest_names[['Name', 'name_length', 'Births']])
        
        # 4.3 Chris analysis - Fixed the logic
        print("\n4.3 Chris Analysis - States Ranked by Percentage:")
        
        # Calculate total births by state
        state_totals = self.names_df.groupby('State')['Births'].sum().reset_index()
        
        # Calculate Chris births by state
        chris_by_state = self.names_df[self.names_df['Name'] == 'Chris'].groupby('State')['Births'].sum().reset_index()
        
        # Merge and calculate percentage
        chris_analysis = state_totals.merge(chris_by_state, on='State', how='left', suffixes=('_total', '_chris'))
        chris_analysis['chris_births'] = chris_analysis['Births_chris'].fillna(0)
        chris_analysis['total_births'] = chris_analysis['Births_total']
        chris_analysis['chris_percentage'] = (chris_analysis['chris_births'] / chris_analysis['total_births']) * 100
        
        # Filter for states with Chris births and sort
        chris_analysis = chris_analysis[chris_analysis['chris_births'] > 0][['State', 'chris_births', 'total_births', 'chris_percentage']]
        chris_analysis = chris_analysis.sort_values('chris_percentage', ascending=False)
        
        print(chris_analysis.round(4))
        
        # Answer the final question
        lowest_chris = chris_analysis.iloc[-1]
        print(f"\nFinal Answer: The state with the smallest percentage of babies named 'Chris' is {lowest_chris['State']} with {lowest_chris['chris_percentage']:.4f}%")
    
    def run_complete_analysis(self):
        """Run all analyses"""
        print("U.S. BABY NAMES ANALYSIS (Direct CSV - Simple Version)")
        print("="*60)
        
        if not self.load_data():
            print("Failed to load data. Please check if names_data.csv exists in the current directory.")
            return
        
        # Run all analyses
        self.analyze_popularity_changes()
        self.analyze_decade_comparisons()
        self.analyze_regional_patterns()
        self.analyze_unique_names()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)
        print("All analysis results have been displayed above.")

# Usage example
if __name__ == "__main__":
    # Initialize the analyzer with CSV file
    analyzer = BabyNamesAnalyzerSimple('names_data.csv')
    
    # Run the complete analysis
    analyzer.run_complete_analysis()
