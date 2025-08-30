import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from mysql.connector import Error
import numpy as np

# Set up the plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class BabyNamesAnalyzer:
    def __init__(self, host='localhost', user='root', password='', database='baby_names_db'):
        """Initialize the analyzer with database connection parameters"""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        
    def connect_to_database(self):
        """Establish connection to MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Successfully connected to MySQL database")
            return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def execute_query(self, query):
        """Execute a SQL query and return results as DataFrame"""
        if not self.connection or not self.connection.is_connected():
            if not self.connect_to_database():
                return None
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            
            cursor.close()
            return pd.DataFrame(results, columns=columns)
        except Error as e:
            print(f"Error executing query: {e}")
            return None
    
    def analyze_popularity_changes(self):
        """Objective 1: Track changes in name popularity"""
        print("\n" + "="*60)
        print("OBJECTIVE 1: TRACKING NAME POPULARITY CHANGES")
        print("="*60)
        
        # 1.1 Overall most popular names and their yearly trends
        query1 = """
        WITH overall_popular_names AS (
            SELECT 
                Name,
                Gender,
                SUM(Births) as total_births
            FROM names
            GROUP BY Name, Gender
            ORDER BY total_births DESC
            LIMIT 2
        ),
        popularity_over_years AS (
            SELECT 
                n.Year,
                n.Name,
                n.Gender,
                n.Births,
                RANK() OVER (PARTITION BY n.Year, n.Gender ORDER BY n.Births DESC) as yearly_rank
            FROM names n
            INNER JOIN overall_popular_names opn ON n.Name = opn.Name AND n.Gender = opn.Gender
        )
        SELECT 
            Year,
            Name,
            Gender,
            Births,
            yearly_rank
        FROM popularity_over_years
        ORDER BY Gender, Year
        """
        
        df1 = self.execute_query(query1)
        if df1 is not None:
            print("\n1.1 Overall Most Popular Names - Yearly Trends:")
            print(df1.head(10))
            
            # Create visualization
            plt.figure(figsize=(12, 6))
            for gender in df1['Gender'].unique():
                gender_data = df1[df1['Gender'] == gender]
                plt.plot(gender_data['Year'], gender_data['Births'], 
                        marker='o', label=f"{gender_data['Name'].iloc[0]} ({gender})")
            
            plt.title('Popularity Trends of Overall Most Popular Names Over Time')
            plt.xlabel('Year')
            plt.ylabel('Number of Births')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('popularity_trends.png', dpi=300, bbox_inches='tight')
            plt.show()
        
        # 1.2 Names with biggest popularity jumps
        query2 = """
        WITH first_last_years AS (
            SELECT 
                MIN(Year) as first_year,
                MAX(Year) as last_year
            FROM names
        ),
        name_popularity_changes AS (
            SELECT 
                n.Name,
                n.Gender,
                SUM(CASE WHEN n.Year = (SELECT first_year FROM first_last_years) THEN n.Births ELSE 0 END) as first_year_births,
                SUM(CASE WHEN n.Year = (SELECT last_year FROM first_last_years) THEN n.Births ELSE 0 END) as last_year_births,
                SUM(CASE WHEN n.Year = (SELECT last_year FROM first_last_years) THEN n.Births ELSE 0 END) - 
                SUM(CASE WHEN n.Year = (SELECT first_year FROM first_last_years) THEN n.Births ELSE 0 END) as popularity_change
            FROM names n
            GROUP BY n.Name, n.Gender
            HAVING first_year_births > 0 AND last_year_births > 0
        )
        SELECT 
            Name,
            Gender,
            first_year_births,
            last_year_births,
            popularity_change
        FROM name_popularity_changes
        ORDER BY popularity_change DESC
        LIMIT 10
        """
        
        df2 = self.execute_query(query2)
        if df2 is not None:
            print("\n1.2 Names with Biggest Popularity Jumps:")
            print(df2)
            
            # Create visualization
            plt.figure(figsize=(12, 8))
            top_names = df2.head(10)
            colors = ['red' if gender == 'F' else 'blue' for gender in top_names['Gender']]
            
            bars = plt.barh(range(len(top_names)), top_names['popularity_change'], 
                           color=colors, alpha=0.7)
            
            plt.yticks(range(len(top_names)), top_names['Name'])
            plt.xlabel('Popularity Change (Births)')
            plt.title('Top 10 Names with Biggest Popularity Jumps')
            plt.grid(True, alpha=0.3)
            
            # Add gender labels
            for i, (name, gender) in enumerate(zip(top_names['Name'], top_names['Gender'])):
                plt.text(top_names['popularity_change'].iloc[i] + 100, i, 
                        f"({gender})", va='center')
            
            plt.tight_layout()
            plt.savefig('popularity_jumps.png', dpi=300, bbox_inches='tight')
            plt.show()
    
    def analyze_decade_comparisons(self):
        """Objective 2: Compare popularity across decades"""
        print("\n" + "="*60)
        print("OBJECTIVE 2: DECADE COMPARISONS")
        print("="*60)
        
        # 2.1 Top 3 names by year
        query1 = """
        WITH yearly_rankings AS (
            SELECT 
                Year,
                Name,
                Gender,
                SUM(Births) as total_births,
                RANK() OVER (PARTITION BY Year, Gender ORDER BY SUM(Births) DESC) as rank_in_year
            FROM names
            GROUP BY Year, Name, Gender
        )
        SELECT 
            Year,
            Name,
            Gender,
            total_births,
            rank_in_year
        FROM yearly_rankings
        WHERE rank_in_year <= 3
        ORDER BY Year, Gender, rank_in_year
        """
        
        df1 = self.execute_query(query1)
        if df1 is not None:
            print("\n2.1 Top 3 Names by Year (Sample):")
            print(df1.head(15))
        
        # 2.2 Top 3 names by decade
        query2 = """
        WITH decade_data AS (
            SELECT 
                CONCAT(FLOOR(Year/10)*10, 's') as decade,
                Name,
                Gender,
                SUM(Births) as total_births,
                RANK() OVER (PARTITION BY CONCAT(FLOOR(Year/10)*10, 's'), Gender ORDER BY SUM(Births) DESC) as rank_in_decade
            FROM names
            GROUP BY CONCAT(FLOOR(Year/10)*10, 's'), Name, Gender
        )
        SELECT 
            decade,
            Name,
            Gender,
            total_births,
            rank_in_decade
        FROM decade_data
        WHERE rank_in_decade <= 3
        ORDER BY decade, Gender, rank_in_decade
        """
        
        df2 = self.execute_query(query2)
        if df2 is not None:
            print("\n2.2 Top 3 Names by Decade:")
            print(df2)
            
            # Create visualization
            plt.figure(figsize=(15, 10))
            
            # Create subplots for each gender
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
            
            # Girls
            girls_data = df2[df2['Gender'] == 'F']
            girls_pivot = girls_data.pivot(index='decade', columns='rank_in_decade', values='Name')
            
            girls_pivot.plot(kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
            ax1.set_title('Top 3 Girl Names by Decade')
            ax1.set_ylabel('Name')
            ax1.legend(['1st Place', '2nd Place', '3rd Place'])
            ax1.tick_params(axis='x', rotation=45)
            
            # Boys
            boys_data = df2[df2['Gender'] == 'M']
            boys_pivot = boys_data.pivot(index='decade', columns='rank_in_decade', values='Name')
            
            boys_pivot.plot(kind='bar', ax=ax2, color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
            ax2.set_title('Top 3 Boy Names by Decade')
            ax2.set_ylabel('Name')
            ax2.legend(['1st Place', '2nd Place', '3rd Place'])
            ax2.tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            plt.savefig('decade_comparisons.png', dpi=300, bbox_inches='tight')
            plt.show()
    
    def analyze_regional_patterns(self):
        """Objective 3: Compare popularity across regions"""
        print("\n" + "="*60)
        print("OBJECTIVE 3: REGIONAL ANALYSIS")
        print("="*60)
        
        # 3.1 Babies born by region
        query1 = """
        SELECT 
            r.Region,
            SUM(n.Births) as total_births
        FROM names n
        JOIN regions r ON n.State = r.State
        GROUP BY r.Region
        ORDER BY total_births DESC
        """
        
        df1 = self.execute_query(query1)
        if df1 is not None:
            print("\n3.1 Number of Babies Born by Region:")
            print(df1)
            
            # Create visualization
            plt.figure(figsize=(10, 8))
            colors = plt.cm.Set3(np.linspace(0, 1, len(df1)))
            plt.pie(df1['total_births'], labels=df1['Region'], autopct='%1.1f%%', 
                   colors=colors, startangle=90)
            plt.title('Distribution of Babies Born by Region')
            plt.axis('equal')
            plt.savefig('regional_distribution.png', dpi=300, bbox_inches='tight')
            plt.show()
        
        # 3.2 Top names by region
        query2 = """
        WITH regional_rankings AS (
            SELECT 
                r.Region,
                n.Name,
                n.Gender,
                SUM(n.Births) as total_births,
                RANK() OVER (PARTITION BY r.Region, n.Gender ORDER BY SUM(n.Births) DESC) as rank_in_region
            FROM names n
            JOIN regions r ON n.State = r.State
            GROUP BY r.Region, n.Name, n.Gender
        )
        SELECT 
            Region,
            Name,
            Gender,
            total_births,
            rank_in_region
        FROM regional_rankings
        WHERE rank_in_region <= 3
        ORDER BY Region, Gender, rank_in_region
        """
        
        df2 = self.execute_query(query2)
        if df2 is not None:
            print("\n3.2 Top 3 Names by Region:")
            print(df2)
            
            # Create visualization
            plt.figure(figsize=(16, 12))
            
            regions = df2['Region'].unique()
            n_regions = len(regions)
            
            fig, axes = plt.subplots(2, 3, figsize=(20, 12))
            axes = axes.flatten()
            
            for i, region in enumerate(regions):
                region_data = df2[df2['Region'] == region]
                
                # Separate girls and boys
                girls = region_data[region_data['Gender'] == 'F'].head(3)
                boys = region_data[region_data['Gender'] == 'M'].head(3)
                
                x = np.arange(3)
                width = 0.35
                
                axes[i].bar(x - width/2, girls['total_births'], width, label='Girls', color='pink', alpha=0.7)
                axes[i].bar(x + width/2, boys['total_births'], width, label='Boys', color='lightblue', alpha=0.7)
                
                axes[i].set_title(f'{region}')
                axes[i].set_ylabel('Total Births')
                axes[i].legend()
                axes[i].set_xticks(x)
                axes[i].set_xticklabels([f'1st\n{girls["Name"].iloc[0]}\n{boys["Name"].iloc[0]}',
                                       f'2nd\n{girls["Name"].iloc[1]}\n{boys["Name"].iloc[1]}',
                                       f'3rd\n{girls["Name"].iloc[2]}\n{boys["Name"].iloc[2]}'])
            
            plt.tight_layout()
            plt.savefig('regional_top_names.png', dpi=300, bbox_inches='tight')
            plt.show()
    
    def analyze_unique_names(self):
        """Objective 4: Explore unique names in the dataset"""
        print("\n" + "="*60)
        print("OBJECTIVE 4: UNIQUE NAMES ANALYSIS")
        print("="*60)
        
        # 4.1 Most popular androgynous names
        query1 = """
        WITH androgynous_names AS (
            SELECT 
                Name,
                SUM(CASE WHEN Gender = 'F' THEN Births ELSE 0 END) as female_births,
                SUM(CASE WHEN Gender = 'M' THEN Births ELSE 0 END) as male_births,
                SUM(Births) as total_births
            FROM names
            GROUP BY Name
            HAVING SUM(CASE WHEN Gender = 'F' THEN Births ELSE 0 END) > 0 
               AND SUM(CASE WHEN Gender = 'M' THEN Births ELSE 0 END) > 0
        )
        SELECT 
            Name,
            female_births,
            male_births,
            total_births
        FROM androgynous_names
        ORDER BY total_births DESC
        LIMIT 10
        """
        
        df1 = self.execute_query(query1)
        if df1 is not None:
            print("\n4.1 Most Popular Androgynous Names:")
            print(df1)
            
            # Create visualization
            plt.figure(figsize=(12, 8))
            x = np.arange(len(df1))
            width = 0.35
            
            plt.bar(x - width/2, df1['female_births'], width, label='Female Births', color='pink', alpha=0.7)
            plt.bar(x + width/2, df1['male_births'], width, label='Male Births', color='lightblue', alpha=0.7)
            
            plt.xlabel('Names')
            plt.ylabel('Number of Births')
            plt.title('Top 10 Most Popular Androgynous Names')
            plt.xticks(x, df1['Name'], rotation=45, ha='right')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('androgynous_names.png', dpi=300, bbox_inches='tight')
            plt.show()
        
        # 4.2 Name length analysis
        query2 = """
        WITH name_lengths AS (
            SELECT 
                Name,
                LENGTH(Name) as name_length,
                SUM(Births) as total_births
            FROM names
            GROUP BY Name
        ),
        length_stats AS (
            SELECT 
                MIN(name_length) as shortest_length,
                MAX(name_length) as longest_length
            FROM name_lengths
        )
        SELECT 
            'Shortest Names' as category,
            Name,
            name_length,
            total_births
        FROM name_lengths, length_stats
        WHERE name_length = shortest_length
        ORDER BY total_births DESC
        LIMIT 5

        UNION ALL

        SELECT 
            'Longest Names' as category,
            Name,
            name_length,
            total_births
        FROM name_lengths, length_stats
        WHERE name_length = longest_length
        ORDER BY total_births DESC
        LIMIT 5
        """
        
        df2 = self.execute_query(query2)
        if df2 is not None:
            print("\n4.2 Name Length Analysis:")
            print(df2)
        
        # 4.3 Chris analysis
        query3 = """
        WITH chris_data AS (
            SELECT 
                n.State,
                SUM(CASE WHEN n.Name = 'Chris' THEN n.Births ELSE 0 END) as chris_births,
                SUM(n.Births) as total_births,
                (SUM(CASE WHEN n.Name = 'Chris' THEN n.Births ELSE 0 END) * 100.0 / SUM(n.Births)) as chris_percentage
            FROM names n
            GROUP BY n.State
            HAVING SUM(n.Births) > 0
        )
        SELECT 
            State,
            chris_births,
            total_births,
            ROUND(chris_percentage, 4) as chris_percentage
        FROM chris_data
        ORDER BY chris_percentage DESC
        """
        
        df3 = self.execute_query(query3)
        if df3 is not None:
            print("\n4.3 Chris Analysis - States Ranked by Percentage:")
            print(df3)
            
            # Create visualization
            plt.figure(figsize=(12, 8))
            top_states = df3.head(10)
            
            bars = plt.bar(range(len(top_states)), top_states['chris_percentage'], 
                          color='skyblue', alpha=0.7)
            
            plt.xlabel('States')
            plt.ylabel('Percentage of Babies Named Chris')
            plt.title('Top 10 States with Highest Percentage of Babies Named Chris')
            plt.xticks(range(len(top_states)), top_states['State'], rotation=45)
            plt.grid(True, alpha=0.3)
            
            # Add percentage labels on bars
            for i, bar in enumerate(bars):
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.4f}%', ha='center', va='bottom')
            
            plt.tight_layout()
            plt.savefig('chris_analysis.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            # Answer the final question
            print(f"\nFinal Answer: The state with the smallest percentage of babies named 'Chris' is {df3.iloc[-1]['State']} with {df3.iloc[-1]['chris_percentage']:.4f}%")
    
    def run_complete_analysis(self):
        """Run all analyses"""
        print("U.S. BABY NAMES ANALYSIS")
        print("="*60)
        
        if not self.connect_to_database():
            print("Failed to connect to database. Please check your connection parameters.")
            return
        
        # Run all analyses
        self.analyze_popularity_changes()
        self.analyze_decade_comparisons()
        self.analyze_regional_patterns()
        self.analyze_unique_names()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)
        print("All visualizations have been saved as PNG files.")
        
        if self.connection and self.connection.is_connected():
            self.connection.close()

# Usage example
if __name__ == "__main__":
    # Initialize the analyzer (update connection parameters as needed)
    analyzer = BabyNamesAnalyzer(
        host='localhost',
        user='root',
        password='',  # Update with your password if needed
        database='baby_names_db'
    )
    
    # Run the complete analysis
    analyzer.run_complete_analysis()
