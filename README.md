# Game Analysis Visualization System

## Overview

This project provides a comprehensive analysis system for comparing mobile puzzle games, specifically Royal Match and Toon Blast. The system includes data collection, analysis, visualization generation, and an interactive web viewer for exploring the findings.

## Project Structure

```
dream-case/
├── game-analysis/               # Core analysis scripts and data [↓](#game-analysis-details)
│   ├── game_analysis.py         # Main analysis script
│   ├── game-analysis-toon-blast.json  # Toon Blast game data
│   ├── game-analysis-royal-match.json # Royal Match game data
│   ├── game_analysis.png        # Generated analysis image
│   ├── game_analysis_additional.png  # Additional analysis image
│   └── requirements.txt         # Python dependencies
│
├── general-analyze/             # Visualization and advanced analysis [↓](#general-analyze-details)
│   ├── complete-analysis.md     # Executive summary and comprehensive game comparison [↓](#complete-analysis)
│   ├── difficulty-tracker.md    # Detailed tracking of difficulty progression by level [↓](#difficulty-tracker)
│   ├── distribution-analysis.md # Obstacle and power-up distribution statistics [↓](#distribution-analysis)
│   ├── final-recommendations.md # Strategic recommendations for both games [↓](#final-recommendations)
│   ├── game-puanting.md         # Analysis of when games ask for ratings [↓](#game-puanting)
│   ├── game-insights.md         # Initial observations and key differences [↓](#game-insights)
│   ├── mechanics-comparison.md  # Detailed side-by-side mechanics comparison [↓](#mechanics-comparison)
│   ├── ui-analysis.md           # User experience and interface design analysis [↓](#ui-analysis)
│   └── visual-analysis/         # Visual representation of game data [↓](#visual-analysis-details)
│       ├── enhanced-visualization.py         # Original visualization script with hardcoded data
│       ├── enhanced-visualization-json.py    # Updated script that loads data from JSON files
│       ├── game_charts_viewer.html           # Web-based visualization viewer
│       └── game_charts/                      # Generated visualization images [↓](#generated-visualizations)
│           ├── move_analysis.png             # Analysis of move counts
│           ├── power_up_analysis.png         # Power-up distribution analysis
│           ├── obstacle_distribution.png     # Obstacle variety analysis
│           ├── difficulty_progression.png    # Difficulty curve mapping
│           ├── master_dashboard.png          # Consolidated metrics view
│           ├── monetization_difficulty_correlation.png  # Monetization analysis
│           ├── obstacle_timing.png           # Obstacle introduction timing
│           └── retention_monetization.png    # Retention feature analysis
│
├── royal-match/                 # Royal Match specific analysis [↓](#royal-match-details)
│   ├── game-levels/             # 40 analyzed game levels with detailed data
│   ├── gameplay-guide/          # Comprehensive gameplay documentation
│   │   └── gameplay-guide.md    # Detailed guide with game mechanics
│   ├── tasks&areas/             # Documentation on progression system
│   │   └── tasks-&-areas.md     # Guide for tasks and area completion
│   └── objects/                 # Analysis of game objects/obstacles
│       ├── box/                 # Box obstacle documentation
│       ├── grass/               # Grass obstacle documentation
│       ├── honey/               # Honey obstacle documentation
│       ├── mailbox/             # Mailbox obstacle documentation
│       ├── royal-egg/           # Royal egg obstacle documentation
│       ├── and more...          # Other game obstacles
│
├── toon-blast/                  # Toon Blast specific analysis [↓](#toon-blast-details)
│   ├── game-levels/             # 40 analyzed game levels with detailed data
│   │   └── folder-creator.sh    # Script used to generate level folders
│   └── gameplay-guide/          # Comprehensive gameplay documentation
│       └── gameplay-guide.md    # Detailed guide with game mechanics
│
```

## Game Data Collection

Both games have been extensively analyzed across 40 levels each:

- **Royal Match**: Data from 40 levels analyzing move counts, power tools, obstacles, difficulty progression, monetization touchpoints, and special features.

- **Toon Blast**: Data from 40 levels analyzing move counts, special items, obstacles, difficulty curves, monetization strategies, and special features.

## Visualization System

The visualization system transforms the JSON game data into insightful visualizations that highlight key differences and similarities between the games.

### Main Visualization Scripts

1. **enhanced-visualization.py**: The original script with hardcoded data arrays.
2. **enhanced-visualization-json.py**: The updated script that loads data directly from the JSON files.

## Key Game Differences Uncovered

1. **Level Design Philosophy**:
   - Toon Blast offers higher average move counts (30.7 vs 26.2), creating a more forgiving gameplay experience
   - Royal Match utilizes a wider variety of obstacles to create more diverse gameplay challenges
   - Power tool distribution shows Toon Blast emphasizes explosive effects while Royal Match balances power more evenly

2. **Player Experience**:
   - Toon Blast's higher unused moves (9.5) indicates intentionally easier early levels for player onboarding
   - Royal Match's higher hint usage shows a design philosophy focused on guiding players through complexity
   - Special events create different engagement loops (Crown Rush vs. Butler Gift)

3. **Monetization Approaches**:
   - Different timing of additional move purchases (level 15 for Toon Blast vs. levels 23, 33, and 39 for Royal Match)
   - Both games time special events to create positive reinforcement cycles that encourage re-engagement

## How to Use

### Running the Core Analysis

1. Navigate to the `game-analysis` directory:
   ```bash
   cd dream-case/game-analysis/
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the analysis script:
   ```bash
   python game_analysis.py
   ```

### Generating Visualizations

1. Navigate to the visual analysis directory:
   ```bash
   cd dream-case/general-analyze/visual-analysis/
   ```

2. Run the JSON-based visualization script:
   ```bash
   python enhanced-visualization-json.py
   ```

### Viewing the Visualizations

1. Start a local web server in the visual analysis directory:
   ```bash
   cd /Users/ilkeryoru/Desktop/PERSONAL\ REPOS/dream-case/general-analyze/visual-analysis/
   python -m http.server 8000
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8000/game_charts_viewer.html
   ```

3. The visualization interface will display all generated charts with descriptions and insights.

## Reading the Analysis Documents

To get a comprehensive understanding of the game analysis:

1. Start with **complete-analysis.md** for an executive summary and overview
2. Review **mechanics-comparison.md** for a detailed side-by-side comparison
3. Examine **difficulty-tracker.md** for level-by-level difficulty analysis
4. Study **distribution-analysis.md** for statistics on game elements
5. Read **ui-analysis.md** for insights on user experience design
6. Finish with **final-recommendations.md** for strategic improvement suggestions

## Extending the System

### Adding New Games

To add analysis for a new game:

1. Create a new JSON file in the `game-analysis` directory following the format of existing JSON files
2. Update the `enhanced-visualization-json.py` script to load and process the new game data
3. Modify the visualization generation functions to include the new game in comparisons
4. Regenerate the visualizations by running the script

### Adding New Visualizations

To add new visualization types:

1. Modify the `enhanced-visualization-json.py` script to include new chart generation code
2. Update the `game_charts_viewer.html` file to include the new chart in the web interface

## Dependencies

- Python 3.x
- matplotlib
- numpy
- pandas
- seaborn
- PIL (Python Imaging Library)

## License

This project is for educational and analytical purposes only. 