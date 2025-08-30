-- U.S. Baby Names Analysis
-- Comprehensive analysis covering popularity trends, decade comparisons, regional analysis, and unique names

-- ============================================================================
-- OBJECTIVE 1: Track changes in name popularity
-- ============================================================================

-- 1.1 Overall most popular girl and boy names and their popularity changes over time
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
ORDER BY Gender, Year;

-- 1.2 Names with biggest jumps in popularity from first year to last year
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
LIMIT 10;

-- ============================================================================
-- OBJECTIVE 2: Compare popularity across decades
-- ============================================================================

-- 2.1 Top 3 girl names and top 3 boy names for each year
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
ORDER BY Year, Gender, rank_in_year;

-- 2.2 Top 3 girl names and top 3 boy names for each decade
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
ORDER BY decade, Gender, rank_in_decade;

-- ============================================================================
-- OBJECTIVE 3: Compare popularity across regions
-- ============================================================================

-- 3.1 Number of babies born in each region
SELECT 
    r.Region,
    SUM(n.Births) as total_births
FROM names n
JOIN regions r ON n.State = r.State
GROUP BY r.Region
ORDER BY total_births DESC;

-- 3.2 Top 3 girl names and top 3 boy names within each region
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
ORDER BY Region, Gender, rank_in_region;

-- ============================================================================
-- OBJECTIVE 4: Explore unique names in the dataset
-- ============================================================================

-- 4.1 Most popular androgynous names (names given to both females and males)
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
LIMIT 10;

-- 4.2 Shortest and longest names, and most popular short/long names
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
LIMIT 5;

-- 4.3 State with highest percentage of babies named "Chris"
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
ORDER BY chris_percentage DESC;

-- 4.4 State with smallest percentage of babies named "Chris"
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
ORDER BY chris_percentage ASC;
