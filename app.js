// Utility functions
const formatNumber = (value) => {
    return value.toLocaleString();
};
// Load real names data
let namesData = {};
const loadNamesData = async () => {
    try {
        const response = await fetch('names_data.json');
        if (!response.ok) {
            throw new Error('Failed to load names data');
        }
        namesData = await response.json();
        console.log(`Loaded ${Object.keys(namesData).length} names from dataset`);
    }
    catch (error) {
        console.error('Error loading names data:', error);
        // Fallback to mock data if JSON file is not available
        namesData = {
            'michael': {
                name: 'Michael',
                total_births: 1380000,
                girls_births: 0,
                boys_births: 1380000,
                most_popular_year: 1990,
                most_popular_state: 'CA',
                popularity_rank: 1,
                gender_distribution: '100% Boys'
            },
            'jessica': {
                name: 'Jessica',
                total_births: 863000,
                girls_births: 863000,
                boys_births: 0,
                most_popular_year: 1985,
                most_popular_state: 'TX',
                popularity_rank: 1,
                gender_distribution: '100% Girls'
            }
        };
    }
};
// Mock data (in a real app, this would come from an API)
const mockResults = {
    popularity_changes: {
        top_names: {
            girls: { name: 'Jessica', births: 863000 },
            boys: { name: 'Michael', births: 1380000 }
        },
        biggest_increases: [
            { Name: 'Isabella', Gender: 'F', popularity_change: 22266 },
            { Name: 'Sophia', Gender: 'F', popularity_change: 18900 },
            { Name: 'Emma', Gender: 'F', popularity_change: 16500 },
            { Name: 'Olivia', Gender: 'F', popularity_change: 14200 },
            { Name: 'Ava', Gender: 'F', popularity_change: 12000 }
        ],
        biggest_decreases: [
            { Name: 'Jessica', Gender: 'F', popularity_change: -45000 },
            { Name: 'Ashley', Gender: 'F', popularity_change: -38000 },
            { Name: 'Amanda', Gender: 'F', popularity_change: -32000 },
            { Name: 'Sarah', Gender: 'F', popularity_change: -28000 },
            { Name: 'Jennifer', Gender: 'F', popularity_change: -25000 }
        ]
    },
    regional_patterns: {
        regional_births: [
            { Region: 'South', Births: 34200000 },
            { Region: 'Midwest', Births: 29800000 },
            { Region: 'Mid_Atlantic', Births: 24500000 },
            { Region: 'Pacific', Births: 19800000 },
            { Region: 'Mountain', Births: 8900000 },
            { Region: 'New_England', Births: 7600000 }
        ]
    },
    unique_names: {
        androgynous_names: [
            { Name: 'Casey', F: 45000, M: 38000, total_births: 83000 },
            { Name: 'Riley', F: 42000, M: 35000, total_births: 77000 },
            { Name: 'Jordan', F: 38000, M: 32000, total_births: 70000 },
            { Name: 'Avery', F: 35000, M: 28000, total_births: 63000 },
            { Name: 'Morgan', F: 32000, M: 25000, total_births: 57000 }
        ],
        final_answer: {
            state: 'WV',
            percentage: 0.0018
        },
        noah_analysis: [
            { State: 'CA', noah_births: 45000, total_births: 19800000, noah_percentage: 0.2273 },
            { State: 'TX', noah_births: 38000, total_births: 15600000, noah_percentage: 0.2436 },
            { State: 'NY', noah_births: 32000, total_births: 12500000, noah_percentage: 0.2560 },
            { State: 'FL', noah_births: 28000, total_births: 9800000, noah_percentage: 0.2857 },
            { State: 'IL', noah_births: 25000, total_births: 8500000, noah_percentage: 0.2941 },
            { State: 'PA', noah_births: 22000, total_births: 7500000, noah_percentage: 0.2933 },
            { State: 'OH', noah_births: 20000, total_births: 6800000, noah_percentage: 0.2941 },
            { State: 'MI', noah_births: 18000, total_births: 6200000, noah_percentage: 0.2903 },
            { State: 'GA', noah_births: 16000, total_births: 5800000, noah_percentage: 0.2759 },
            { State: 'NC', noah_births: 15000, total_births: 5200000, noah_percentage: 0.2885 }
        ]
    },
    summary: {
        total_records: 2200000,
        years_covered: '1980 - 2010',
        states_covered: 50,
        analysis_date: new Date().toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        })
    }
};
// Search functionality
const searchName = () => {
    const searchInput = document.getElementById('nameSearch');
    const searchResults = document.getElementById('searchResults');
    const name = searchInput.value.trim().toLowerCase();
    
    if (!name) {
        alert('Please enter a name to search');
        return;
    }
    
    const result = namesData[name];
    
    if (result) {
        searchResults.innerHTML = `
            <div class="search-result-container">
                <div class="result-header">
                    <div class="name-display">
                        <h2 class="name-title">${result.name}</h2>
                        <div class="name-badge">
                            <span class="badge ${result.gender_distribution.includes('Boys') ? 'badge-blue' : result.gender_distribution.includes('Girls') ? 'badge-pink' : 'badge-purple'}">
                                ${result.gender_distribution.includes('Boys') ? '♂ Boy' : result.gender_distribution.includes('Girls') ? '♀ Girl' : '⚧ Unisex'}
                            </span>
                        </div>
                    </div>
                    <div class="rank-badge">
                        <span class="rank-number">#${result.popularity_rank}</span>
                        <span class="rank-label">Popularity Rank</span>
                    </div>
                </div>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon">
                            <i class="fas fa-baby"></i>
                        </div>
                        <div class="stat-content">
                            <div class="stat-value">${formatNumber(result.total_births)}</div>
                            <div class="stat-label">Total Births</div>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon">
                            <i class="fas fa-calendar-alt"></i>
                        </div>
                        <div class="stat-content">
                            <div class="stat-value">${result.most_popular_year}</div>
                            <div class="stat-label">Peak Year</div>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div class="stat-content">
                            <div class="stat-value">${result.most_popular_state}</div>
                            <div class="stat-label">Top State</div>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon">
                            <i class="fas fa-venus-mars"></i>
                        </div>
                        <div class="stat-content">
                            <div class="stat-value">${result.gender_distribution}</div>
                            <div class="stat-label">Distribution</div>
                        </div>
                    </div>
                </div>
                
                <div class="result-footer">
                    <div class="insight-card">
                        <div class="insight-header">
                            <i class="fas fa-lightbulb"></i>
                            <span>Quick Insight</span>
                        </div>
                        <p class="insight-text">
                            ${result.name} has been given to ${formatNumber(result.total_births)} babies in the United States, 
                            making it the ${result.popularity_rank}${getOrdinalSuffix(result.popularity_rank)} most popular name overall. 
                            It reached peak popularity in ${result.most_popular_year} and is most common in ${result.most_popular_state}.
                        </p>
                    </div>
                </div>
            </div>
        `;
        searchResults.classList.add('show');
    } else {
        searchResults.innerHTML = `
            <div class="search-result-container">
                <div class="not-found-card">
                    <div class="not-found-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <h3 class="not-found-title">Name Not Found</h3>
                    <p class="not-found-text">
                        The name "<strong>${name}</strong>" was not found in our database.
                    </p>
                    <p class="not-found-hint">
                        Try searching for a different name. We have data for over 22,000 unique names!
                    </p>
                    <div class="suggestions">
                        <span class="suggestion-label">Popular names to try:</span>
                        <div class="suggestion-tags">
                            <span class="suggestion-tag" onclick="searchSuggestion('michael')">Michael</span>
                            <span class="suggestion-tag" onclick="searchSuggestion('jessica')">Jessica</span>
                            <span class="suggestion-tag" onclick="searchSuggestion('emma')">Emma</span>
                            <span class="suggestion-tag" onclick="searchSuggestion('james')">James</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
        searchResults.classList.add('show');
    }
};

// Helper function to get ordinal suffix
const getOrdinalSuffix = (num) => {
    const j = num % 10;
    const k = num % 100;
    if (j === 1 && k !== 11) return 'st';
    if (j === 2 && k !== 12) return 'nd';
    if (j === 3 && k !== 13) return 'rd';
    return 'th';
};

// Function to handle suggestion clicks
const searchSuggestion = (name) => {
    document.getElementById('nameSearch').value = name;
    searchName();
};
// DOM manipulation functions
const populateSummary = (summary) => {
    const summaryGrid = document.getElementById('summaryGrid');
    if (!summaryGrid)
        return;
    summaryGrid.innerHTML = `
    <div class="summary-card">
      <h3>${formatNumber(summary.total_records)}</h3>
      <p>Total Records</p>
    </div>
    <div class="summary-card">
      <h3>${summary.years_covered}</h3>
      <p>Years Covered</p>
    </div>
    <div class="summary-card">
      <h3>${summary.states_covered}</h3>
      <p>States Analyzed</p>
    </div>
  `;
};
const populateTopNames = (topNames) => {
    const topNamesElement = document.getElementById('topNames');
    if (!topNamesElement)
        return;
    topNamesElement.innerHTML = `
    <div class="highlight-box">
      <h3>Overall Champions</h3>
      <p><strong>${topNames.girls.name}</strong> leads for girls with ${formatNumber(topNames.girls.births)} total births</p>
      <p><strong>${topNames.boys.name}</strong> leads for boys with ${formatNumber(topNames.boys.births)} total births</p>
    </div>
  `;
};
const populatePopularityChanges = (increases, decreases) => {
    const increasesTable = document.getElementById('biggestIncreases');
    const decreasesTable = document.getElementById('biggestDecreases');
    if (increasesTable) {
        increasesTable.innerHTML = `
      <thead>
        <tr>
          <th>Name</th>
          <th>Gender</th>
          <th>Change</th>
        </tr>
      </thead>
      <tbody>
        ${increases.map(item => `
          <tr>
            <td>${item.Name}</td>
            <td><span class="badge badge-${item.Gender === 'F' ? 'girl' : 'boy'}">${item.Gender === 'F' ? 'Girl' : 'Boy'}</span></td>
            <td>+${formatNumber(item.popularity_change)}</td>
          </tr>
        `).join('')}
      </tbody>
    `;
    }
    if (decreasesTable) {
        decreasesTable.innerHTML = `
      <thead>
        <tr>
          <th>Name</th>
          <th>Gender</th>
          <th>Change</th>
        </tr>
      </thead>
      <tbody>
        ${decreases.map(item => `
          <tr>
            <td>${item.Name}</td>
            <td><span class="badge badge-${item.Gender === 'F' ? 'girl' : 'boy'}">${item.Gender === 'F' ? 'Girl' : 'Boy'}</span></td>
            <td>${formatNumber(item.popularity_change)}</td>
          </tr>
        `).join('')}
      </tbody>
    `;
    }
};
const populateRegionalData = (regionalBirths) => {
    const regionalTable = document.getElementById('regionalData');
    if (!regionalTable)
        return;
    const totalBirths = regionalBirths.reduce((sum, region) => sum + region.Births, 0);
    regionalTable.innerHTML = `
    <thead>
      <tr>
        <th>Region</th>
        <th>Total Births</th>
        <th>Percentage</th>
      </tr>
    </thead>
    <tbody>
      ${regionalBirths.map(region => `
        <tr>
          <td><span class="badge badge-region">${region.Region}</span></td>
          <td>${formatNumber(region.Births)}</td>
          <td>${((region.Births / totalBirths) * 100).toFixed(1)}%</td>
        </tr>
      `).join('')}
    </tbody>
  `;
};
const populateAndrogynousNames = (androgynousNames) => {
    const androgynousTable = document.getElementById('androgynousNames');
    if (!androgynousTable)
        return;
    androgynousTable.innerHTML = `
    <thead>
      <tr>
        <th>Name</th>
        <th>Girl Births</th>
        <th>Boy Births</th>
        <th>Total Births</th>
      </tr>
    </thead>
    <tbody>
      ${androgynousNames.map(name => `
        <tr>
          <td><strong>${name.Name || 'N/A'}</strong></td>
          <td>${formatNumber(name.F)}</td>
          <td>${formatNumber(name.M)}</td>
          <td>${formatNumber(name.total_births)}</td>
        </tr>
      `).join('')}
    </tbody>
  `;
};
const populateNoahAnalysis = (finalAnswer, noahAnalysis) => {
    const noahAnswer = document.getElementById('noahAnswer');
    const noahTable = document.getElementById('noahAnalysis');
    if (noahAnswer) {
        noahAnswer.innerHTML = `
      <h3>The Answer to Our Question</h3>
      <p><strong>${finalAnswer.state}</strong> has the smallest percentage of babies named 'Noah' at <strong>${finalAnswer.percentage}%</strong></p>
    `;
    }
    if (noahTable) {
        noahTable.innerHTML = `
      <thead>
        <tr>
          <th>State</th>
          <th>Noah Births</th>
          <th>Total Births</th>
          <th>Percentage</th>
        </tr>
      </thead>
      <tbody>
        ${noahAnalysis.slice(0, 10).map(state => `
          <tr>
            <td><strong>${state.State}</strong></td>
            <td>${formatNumber(state.noah_births)}</td>
            <td>${formatNumber(state.total_births)}</td>
            <td>${state.noah_percentage.toFixed(4)}%</td>
          </tr>
        `).join('')}
      </tbody>
    `;
    }
};
// Main initialization function
const initializeApp = async () => {
    try {
        // Load names data first
        await loadNamesData();
        // Populate all sections with data
        populateSummary(mockResults.summary);
        populateTopNames(mockResults.popularity_changes.top_names);
        populatePopularityChanges(mockResults.popularity_changes.biggest_increases, mockResults.popularity_changes.biggest_decreases);
        populateRegionalData(mockResults.regional_patterns.regional_births);
        populateAndrogynousNames(mockResults.unique_names.androgynous_names);
        populateNoahAnalysis(mockResults.unique_names.final_answer, mockResults.unique_names.noah_analysis);
        console.log('Baby Names Analysis Dashboard loaded successfully!');
        console.log(`Search database contains ${Object.keys(namesData).length} names`);
    }
    catch (error) {
        console.error('Error initializing app:', error);
        document.body.innerHTML = `
      <div class="container">
        <div class="error">
          <h2>Error Loading Data</h2>
          <p>Failed to load analysis results. Please refresh the page.</p>
        </div>
      </div>
    `;
    }
};
// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeApp);
// Make functions globally available
window.searchName = searchName;
window.searchSuggestion = searchSuggestion;
