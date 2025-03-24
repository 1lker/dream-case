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
│   ├── game-objects.md          # Detailed game objects documentation
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
├── game-objects.md              # High-level game analysis document with comparative analysis
└── tree.md                      # Project directory structure documentation
```

## Key Documentation Files

- **game-objects.md**: Contains a comprehensive comparative analysis of both games, including game mechanics, progression systems, player psychology insights, key findings, and detailed recommendations.
- **game-analysis/game-objects.md**: Specific documentation about the game objects found in the analysis.
- **royal-match/gameplay-guide/gameplay-guide.md**: Detailed guide explaining Royal Match mechanics, including:
  - Basic gameplay
  - Lives system
  - Power-ups and combinations
  - Boosters (pre-level and in-game)
  - Resources (coins, bonus levels)
  - Special features (Butler's Gift system)
- **toon-blast/gameplay-guide/gameplay-guide.md**: Detailed guide explaining Toon Blast mechanics, including:
  - Basic gameplay
  - Lives system
  - Special items and combinations
  - Boosters and obstacles
  - Game progress (Champions League)
- **royal-match/tasks&areas/tasks-&-areas.md**: Documentation on Royal Match's progression system with task completion and area unlocking.

## Detailed Analysis Documents

<a id="general-analyze-details"></a>
### General Analyze Directory

The `general-analyze` directory contains a comprehensive set of analysis documents that explore different aspects of both games:

<a id="complete-analysis"></a>
#### Complete Analysis

**File: complete-analysis.md**

This document provides an executive summary and methodical analysis of the games, including:

- **Executive Summary**: High-level comparison of both games
- **Methodology**: Approach used for analyzing all 40 levels of each game
- **Game Mechanics Analysis**: Detailed breakdown of core mechanics with comparative tables
- **Level Design Analysis**: Analysis of level groups, objectives, and strategic challenges
- **Difficulty Progression**: Charts showing difficulty ratings and success rates
- **Graphics Analysis**: Comparison of visual elements and their effectiveness
- **User Interface Analysis**: Evaluation of UI components and accessibility
- **Player Engagement Mechanisms**: Analysis of reward systems and monetization strategies
- **Key Findings and Conclusions**: Strengths of each game and best practices identified

<a id="difficulty-tracker"></a>
#### Difficulty Tracker

**File: difficulty-tracker.md**

This document tracks difficulty progression level-by-level for both games, including:

- **Difficulty Rating Scale**: 1-5 scale for each level (1 being very easy, 5 being very challenging)
- **Complete Level Tables**: Tables for all 40 levels of each game showing:
  - Difficulty ratings
  - Move counts
  - Key difficulty factors
  - Design observations
- **Difficulty Curve Analysis**: Visualization references for difficulty progression

<a id="distribution-analysis"></a>
#### Distribution Analysis

**File: distribution-analysis.md**

Statistical breakdown of game elements and their distribution:

- **Move Count Analysis**: Averages, unused moves, and segment distribution
- **Obstacle Distribution**: Counts and level appearances for all obstacle types
- **Power Tool Usage**: Statistics on frequency and preferences
- **Comparative Analysis**: Side-by-side comparison of distribution patterns between games

<a id="final-recommendations"></a>
#### Final Recommendations

**File: final-recommendations.md**

Comprehensive findings and strategic recommendations for both games:

- **Executive Summary**: Key differences between the games
- **Core Game Design Analysis**: Mechanical differences, difficulty progression, power-up systems
- **Monetization Strategies**: Revenue streams, strategic difficulty, reward systems
- **Player Retention Techniques**: Short-term, mid-term, and long-term retention approaches
- **User Experience Design**: Visual style, interface design, accessibility
- **Strategic Recommendations**: Specific improvements for each game
- **Game Design Insights**: Best practices for future game development

<a id="game-puanting"></a>
#### Game Rating Analysis

**File: game-puanting.md**

Analysis of when each game asks for ratings:
- Royal Match requests ratings at level 15
- Toon Blast requests ratings at level 11
- Insights into early retention strategies

<a id="game-insights"></a>
#### Game Insights

**File: game-insights.md**

Initial observations about both games:

- **Game Mechanics**: Core gameplay, special pieces, power-ups, level goals
- **Level Design Patterns**: Progression and teaching approaches
- **Graphics & Visual Style**: Art direction and visual feedback
- **User Interface**: Layout and tutorial elements
- **Key Differences**: Highlights of major differences between the games

<a id="mechanics-comparison"></a>
#### Mechanics Comparison

**File: mechanics-comparison.md**

Detailed side-by-side comparison tables of game features:

- **Core Gameplay**: Basic mechanics and board interaction
- **Power-ups/Special Items**: Creation methods and effects
- **Boosters**: Types and acquisition methods
- **Obstacles**: Description and first appearance levels
- **Retention Features**: Reward systems and progress tracking
- **Lives System**: Standard lives and regeneration rates
- **Monetization Touchpoints**: Additional moves, boosters, premium options
- **Visual & Aesthetic Design**: Art style and animation focus

<a id="ui-analysis"></a>
#### UI Analysis

**File: ui-analysis.md**

In-depth analysis of user experience and interface design:

- **Game Interface Anatomy**: Breakdown of screen elements
- **UI Design Comparison**: Color palette, typography, animation style
- **UX Patterns and Flows**: Core gameplay loops and onboarding processes
- **Accessibility and Usability**: Strengths and areas for improvement
- **UI/UX Impact on Retention**: Visual progression and satisfaction triggers
- **Comparative Analysis**: Information architecture, visual hierarchy, interaction design

<a id="visual-analysis-details"></a>
### Visual Analysis System

<a id="generated-visualizations"></a>
#### Generated Visualizations

The system produces the following visualizations, saved in the `game_charts/` directory:

1. **move_analysis.png**: Analysis of move counts and difficulty levels across game segments, showing how each game paces player challenge.
2. **power_up_analysis.png**: Breakdown of power-ups in each game, their effects, and frequency, revealing different approaches to player empowerment.
3. **obstacle_distribution.png**: Analysis of obstacle variety and frequency, demonstrating complexity differences between games.
4. **difficulty_progression.png**: Difficulty curve mapping across all levels, highlighting different pacing strategies.
5. **master_dashboard.png**: Consolidated view of all key metrics for quick comparison between games.
6. **monetization_difficulty_correlation.png**: Relationship between difficulty spikes and monetization opportunities, revealing monetization strategies.
7. **obstacle_timing.png**: Timeline of obstacle introduction throughout the games, showing progression complexity.
8. **retention_monetization.png**: Timing and strategy of retention features, comparing engagement approaches.

<a id="game-analysis-details"></a>
### Game Analysis Directory

The `game-analysis` directory contains the core analysis scripts and data files:

- **game_analysis.py**: The main Python script that processes JSON game data and generates analysis reports
- **JSON Data Files**: Structured data for both games with level-by-level information
- **Generated Images**: Analysis visualizations produced by the script
- **Documentation**: Detailed explanation of game objects and their properties

<a id="royal-match-details"></a>
### Royal Match Analysis

The `royal-match` directory contains Royal Match specific analysis:

- **Game Levels**: 40 analyzed levels with detailed data on move counts, obstacles, and difficulty
- **Gameplay Guide**: Comprehensive documentation of game mechanics
- **Tasks & Areas System**: Documentation on progression and reward systems
- **Objects Analysis**: Detailed breakdown of obstacle types and their behavior

<a id="toon-blast-details"></a>
### Toon Blast Analysis

The `toon-blast` directory contains Toon Blast specific analysis:

- **Game Levels**: 40 analyzed levels with detailed data on move counts, obstacles, and difficulty  
- **Gameplay Guide**: Comprehensive documentation of game mechanics including the tap-to-clear system
- **Level Generation**: Script used to create the level analysis structure

## Game Data Collection

Both games have been extensively analyzed across 35-40 levels each:

- **Royal Match**: Data from 40 levels analyzing:
  - Move counts
  - Power tool types and distribution
  - Obstacle types and complexity
  - Difficulty progression
  - Monetization touchpoints
  - Special features (Butler's Gift)

- **Toon Blast**: Data from 35 levels analyzing:
  - Move counts
  - Special item types and creation
  - Obstacle variety and complexity
  - Difficulty curves
  - Monetization strategies
  - Special features (Crown Rush)

The data is stored in JSON format in the `game-analysis` directory, with individual level breakdowns available in each game's respective `game-levels` directory.

## Visualization System

The visualization system transforms the JSON game data into insightful visualizations that highlight key differences and similarities between the games.

### Main Visualization Scripts

1. **enhanced-visualization.py**: The original script with hardcoded data arrays.
2. **enhanced-visualization-json.py**: The updated script that loads data directly from the JSON files and generates visualizations based on that data.

### Generated Visualizations

The system produces the following visualizations, saved in the `game_charts/` directory:

1. **move_analysis.png**: Analysis of move counts and difficulty levels across game segments, showing how each game paces player challenge.
2. **power_up_analysis.png**: Breakdown of power-ups in each game, their effects, and frequency, revealing different approaches to player empowerment.
3. **obstacle_distribution.png**: Analysis of obstacle variety and frequency, demonstrating complexity differences between games.
4. **difficulty_progression.png**: Difficulty curve mapping across all levels, highlighting different pacing strategies.
5. **master_dashboard.png**: Consolidated view of all key metrics for quick comparison between games.
6. **monetization_difficulty_correlation.png**: Relationship between difficulty spikes and monetization opportunities, revealing monetization strategies.
7. **obstacle_timing.png**: Timeline of obstacle introduction throughout the games, showing progression complexity.
8. **retention_monetization.png**: Timing and strategy of retention features, comparing engagement approaches.

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
   cd /Users/ilkeryoru/Desktop/PERSONAL\ REPOS/dream-case/game-analysis/
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
   cd /Users/ilkeryoru/Desktop/PERSONAL\ REPOS/dream-case/general-analyze/visual-analysis/
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

3. The visualization interface will display all generated charts with descriptions and insights, organized into sections:
   - Game mechanics comparison
   - Player experience analysis
   - Monetization strategy evaluation
   - Overall game design philosophy

## Reading the Analysis Documents

To get a comprehensive understanding of the game analysis:

1. Start with **complete-analysis.md** for an executive summary and overview
2. Review **mechanics-comparison.md** for a detailed side-by-side comparison
3. Examine **difficulty-tracker.md** for level-by-level difficulty analysis
4. Study **distribution-analysis.md** for statistics on game elements
5. Read **ui-analysis.md** for insights on user experience design
6. Finish with **final-recommendations.md** for strategic improvement suggestions

You can access these documents directly in the `general-analyze` directory:

```bash
cd /Users/ilkeryoru/Desktop/PERSONAL\ REPOS/dream-case/general-analyze/
```

## Web Visualization Interface Details

The `game_charts_viewer.html` provides a clean, organized interface for viewing all generated visualizations with the following features:

- **Responsive Design**: Works on desktop and mobile browsers
- **Organized Sections**: Charts grouped by analytical category
- **Interactive Elements**: Charts can be enlarged for detailed viewing
- **Contextual Information**: Each chart includes a description explaining key findings
- **Comparative Analysis**: Side-by-side comparison of both games for each metric

## Extending the System

### Adding New Games

To add analysis for a new game:

1. Create a new JSON file in the `game-analysis` directory following the format of existing JSON files:
   ```json
   {
     "game_name": "New Game Name",
     "levels": [
       {
         "level_number": 1,
         "move_count": 25,
         "power_tools": ["tool1", "tool2"],
         "obstacles": ["obstacle1", "obstacle2"],
         ...
       },
       ...
     ]
   }
   ```

2. Update the `enhanced-visualization-json.py` script to load and process the new game data:
   ```python
   # Add new game path
   new_game_path = os.path.join(json_dir, 'game-analysis-new-game.json')
   
   # Load the new game data
   new_game_data = load_json_data(new_game_path)
   ```

3. Modify the visualization generation functions to include the new game in comparisons.

4. Regenerate the visualizations by running the script.

### Adding New Visualizations

To add new visualization types:

1. Modify the `enhanced-visualization-json.py` script to include new chart generation code:
   ```python
   def generate_new_visualization(game1_data, game2_data, output_dir):
       # Visualization code here
       plt.savefig(os.path.join(output_dir, 'new_visualization.png'))
   ```

2. Update the `game_charts_viewer.html` file to include the new chart in the web interface:
   ```html
   <div class="chart-container">
     <h3>New Visualization Title</h3>
     <p>Description of the new visualization and its insights.</p>
     <img src="game_charts/new_visualization.png" alt="New Visualization">
   </div>
   ```

## Dependencies

- Python 3.x
- matplotlib
- numpy
- pandas
- seaborn
- PIL (Python Imaging Library)

## Contributing

Contributions to extend the analysis to more games or add new visualization types are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Create a pull request with a detailed description of your additions

## License

This project is for educational and analytical purposes only. 