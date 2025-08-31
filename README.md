# U.S. Baby Names Analysis Dashboard

A modern, interactive web application that provides comprehensive analysis of U.S. baby naming trends across 30 years and 50 states. Built with vanilla JavaScript, HTML5, and CSS3, featuring a responsive design and real-time search functionality.

## 🚀 Live Demo

[View Live Application](https://your-netlify-url.netlify.app)

## ✨ Features

### Interactive Name Search
- **Real-time Search**: Search any name from a database of 22,000+ unique names
- **Modern UI**: Shadcn-inspired design with smooth animations and hover effects
- **Comprehensive Results**: Display total births, popularity rank, peak year, top state, and gender distribution
- **Smart Suggestions**: Helpful name suggestions when searches return no results

### Data Visualization
- **Overview Dashboard**: Key statistics including 2.2M+ records, 30 years of data, and 50 states
- **Popularity Analysis**: Most popular names by gender with detailed statistics
- **Trend Analysis**: Names with biggest increases and decreases in popularity
- **Regional Patterns**: Birth distribution across U.S. regions
- **Unique Insights**: Androgynous names analysis and demographic patterns

### Technical Features
- **Responsive Design**: Mobile-first approach with adaptive layouts
- **Performance Optimized**: Efficient data loading and rendering
- **Modern CSS**: Custom properties, flexbox, and grid layouts
- **Accessibility**: Semantic HTML and keyboard navigation support

## 🛠️ Tech Stack

- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Styling**: Custom CSS with CSS Grid, Flexbox, and CSS Custom Properties
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Inter font family (Google Fonts)
- **Data**: JSON-based dataset with 22,000+ names and 2.2M+ records
- **Deployment**: Netlify-ready static site

## 📊 Dataset Overview

- **Total Records**: 2.2M+ baby name records
- **Time Span**: 30 years of historical data
- **Geographic Coverage**: All 50 U.S. states
- **Unique Names**: 22,000+ distinct names
- **Data Points**: State, gender, year, name, and birth count

## 🎯 Key Insights

### Most Popular Names
- **Girls**: Jessica (863K births)
- **Boys**: Michael (1.38M births)

### Notable Trends
- **Biggest Increase**: Isabella (+22,266 births)
- **Regional Leader**: South region (34.2M births)
- **Unique Analysis**: West Virginia has the smallest percentage of babies named "Chris" (0.0018%)

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No server setup required - runs entirely in the browser

### Local Development
```bash
# Clone the repository
git clone https://github.com/noahkhomer18/U.S.-Baby-Names---Trends-Insights.git
cd U.S.-Baby-Names---Trends-Insights

# Start local server (Python 3)
python -m http.server 8000

# Or using Node.js
npx serve .

# Open in browser
open http://localhost:8000
```

### Deployment
This project is designed for easy deployment on static hosting platforms:

**Netlify:**
1. Connect your GitHub repository
2. Set build command: (leave empty for static site)
3. Set publish directory: `.`
4. Deploy!

**GitHub Pages:**
1. Enable GitHub Pages in repository settings
2. Select source branch (main/master)
3. Site will be available at `https://username.github.io/repository-name`

## 📁 Project Structure

```
├── index.html              # Main HTML file (web application)
├── styles.css              # Complete styling with modern design
├── app.js                  # Core JavaScript functionality
├── names_data.json         # Optimized dataset for web consumption
├── names_data.csv          # Original dataset (2.2M+ records)
├── baby_names_analysis_simple.py    # Python analysis script
├── requirements_direct.txt # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md              # This file
```

## 🎨 Design Philosophy

This project demonstrates modern web development best practices:

- **Progressive Enhancement**: Works without JavaScript for basic functionality
- **Mobile-First**: Responsive design that works on all devices
- **Performance**: Optimized data loading and efficient rendering
- **Accessibility**: Semantic HTML and keyboard navigation
- **Modern CSS**: Using latest CSS features like Grid and Custom Properties

## 🔧 Customization

### Adding New Names
1. Update `names_data.json` with new name data
2. Follow the existing data structure:
```json
{
  "name": "Example",
  "total_births": 1000,
  "girls_births": 500,
  "boys_births": 500,
  "most_popular_year": 1995,
  "most_popular_state": "CA",
  "popularity_rank": 150,
  "gender_distribution": "50% Girls, 50% Boys"
}
```

### Styling Changes
- Modify `styles.css` using CSS custom properties for consistent theming
- All colors and spacing are defined in the `:root` selector
- Responsive breakpoints are clearly defined

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 About the Developer

**Noah Khomer** - Full Stack Developer passionate about data visualization and modern web technologies.

- 🌐 [Portfolio](https://noah-khomer.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/noah-khomer-19a935342)
- 🐙 [GitHub](https://github.com/noahkhomer18)

---

*This project showcases advanced JavaScript skills, modern CSS techniques, and the ability to create engaging data visualizations for complex datasets.*
