import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Any
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class GameStats:
    name: str
    total_levels: int
    avg_moves: float
    avg_unused_moves: float
    avg_hint_usage: float
    power_tools_usage: Dict[str, float]
    obstacle_distribution: Dict[str, float]
    special_events: Dict[str, int]
    booster_unlocks: List[str]
    difficulty_progression: List[float]

class GameAnalyzer:
    def __init__(self, toon_blast_path: str, royal_match_path: str):
        with open(toon_blast_path, 'r') as f:
            self.toon_blast_data = json.load(f)
        with open(royal_match_path, 'r') as f:
            self.royal_match_data = json.load(f)
        
        self.toon_blast_stats = self._analyze_game(self.toon_blast_data, "Toon Blast")
        self.royal_match_stats = self._analyze_game(self.royal_match_data, "Royal Match")

    def _analyze_game(self, data: Dict, game_name: str) -> GameStats:
        levels = data['game_analysis']['levels']
        
        # Calculate basic statistics
        total_levels = len(levels)
        moves = [level['move_count'] for level in levels if level.get('move_count') is not None]
        unused_moves = [level.get('unused_moves', 0) if level.get('unused_moves') is not None else 0 for level in levels]
        hint_usage = [level.get('hint_usage', 0) if level.get('hint_usage') is not None else 0 for level in levels]
        
        # Calculate power tools usage
        power_tools = defaultdict(int)
        for level in levels:
            if 'power_tools' in level:
                for tool, count in level['power_tools'].items():
                    if count is not None:
                        power_tools[tool] += count
        
        # Calculate obstacle distribution
        obstacles = defaultdict(int)
        for level in levels:
            if 'obstacles' in level:
                for obstacle, count in level['obstacles'].items():
                    if count is not None and obstacle.lower() != 'none':
                        obstacles[obstacle] += count
        
        # Track special events and booster unlocks
        special_events = defaultdict(int)
        booster_unlocks = []
        for level in levels:
            if 'special_events' in level:
                events = level['special_events']
                for event_type, value in events.items():
                    if isinstance(value, bool) and value:
                        special_events[event_type] += 1
                    elif event_type == 'new_booster_unlocked':
                        booster_unlocks.append(value)
        
        # Calculate difficulty progression (based on move count and unused moves)
        difficulty = []
        for i in range(len(levels)):
            if i > 0:
                prev_moves = levels[i-1].get('move_count', 0)
                curr_moves = levels[i].get('move_count', 0)
                prev_unused = levels[i-1].get('unused_moves', 0)
                curr_unused = levels[i].get('unused_moves', 0)
                
                # Handle None values
                prev_moves = 0 if prev_moves is None else prev_moves
                curr_moves = 0 if curr_moves is None else curr_moves
                prev_unused = 0 if prev_unused is None else prev_unused
                curr_unused = 0 if curr_unused is None else curr_unused
                
                diff_score = (curr_moves - prev_moves) + (prev_unused - curr_unused)
                difficulty.append(diff_score)
            else:
                difficulty.append(0)
        
        # Calculate averages, handling None values
        avg_moves = np.mean(moves) if moves else 0
        avg_unused_moves = np.mean([x for x in unused_moves if x is not None]) if unused_moves else 0
        avg_hint_usage = np.mean([x for x in hint_usage if x is not None]) if hint_usage else 0
        
        return GameStats(
            name=game_name,
            total_levels=total_levels,
            avg_moves=avg_moves,
            avg_unused_moves=avg_unused_moves,
            avg_hint_usage=avg_hint_usage,
            power_tools_usage=dict(power_tools),
            obstacle_distribution=dict(obstacles),
            special_events=dict(special_events),
            booster_unlocks=booster_unlocks,
            difficulty_progression=difficulty
        )

    def generate_comparison_report(self):
        print("\n=== Game Analysis Report ===\n")
        
        # Helper function to format float values safely
        def format_float(value):
            if pd.isna(value) or np.isinf(value):
                return "N/A"
            return f"{value:.1f}"
        
        # Basic Statistics Comparison
        print("1. Basic Statistics:")
        print(f"{'Metric':<20} {'Toon Blast':<15} {'Royal Match':<15}")
        print("-" * 50)
        print(f"{'Total Levels':<20} {self.toon_blast_stats.total_levels:<15} {self.royal_match_stats.total_levels:<15}")
        print(f"{'Average Moves':<20} {format_float(self.toon_blast_stats.avg_moves):<15} {format_float(self.royal_match_stats.avg_moves):<15}")
        print(f"{'Avg Unused Moves':<20} {format_float(self.toon_blast_stats.avg_unused_moves):<15} {format_float(self.royal_match_stats.avg_unused_moves):<15}")
        print(f"{'Avg Hint Usage':<20} {format_float(self.toon_blast_stats.avg_hint_usage):<15} {format_float(self.royal_match_stats.avg_hint_usage):<15}")
        
        # Power Tools Comparison
        print("\n2. Power Tools Usage:")
        print(f"{'Tool':<20} {'Toon Blast':<15} {'Royal Match':<15}")
        print("-" * 50)
        all_tools = set(self.toon_blast_stats.power_tools_usage.keys()) | set(self.royal_match_stats.power_tools_usage.keys())
        for tool in sorted(all_tools):
            tb_count = self.toon_blast_stats.power_tools_usage.get(tool, 0)
            rm_count = self.royal_match_stats.power_tools_usage.get(tool, 0)
            print(f"{tool:<20} {tb_count:<15} {rm_count:<15}")
        
        # Obstacle Distribution
        print("\n3. Obstacle Distribution:")
        print(f"{'Obstacle':<20} {'Toon Blast':<15} {'Royal Match':<15}")
        print("-" * 50)
        all_obstacles = set(self.toon_blast_stats.obstacle_distribution.keys()) | set(self.royal_match_stats.obstacle_distribution.keys())
        for obstacle in sorted(all_obstacles):
            tb_count = self.toon_blast_stats.obstacle_distribution.get(obstacle, 0)
            rm_count = self.royal_match_stats.obstacle_distribution.get(obstacle, 0)
            print(f"{obstacle:<20} {tb_count:<15} {rm_count:<15}")
        
        # Special Events
        print("\n4. Special Events:")
        print(f"{'Event':<20} {'Toon Blast':<15} {'Royal Match':<15}")
        print("-" * 50)
        all_events = set(self.toon_blast_stats.special_events.keys()) | set(self.royal_match_stats.special_events.keys())
        for event in sorted(all_events):
            tb_count = self.toon_blast_stats.special_events.get(event, 0)
            rm_count = self.royal_match_stats.special_events.get(event, 0)
            print(f"{event:<20} {tb_count:<15} {rm_count:<15}")
        
        # Booster Unlocks
        print("\n5. Booster Unlocks:")
        print("Toon Blast:", ", ".join(sorted(self.toon_blast_stats.booster_unlocks)))
        print("Royal Match:", ", ".join(sorted(self.royal_match_stats.booster_unlocks)))
        
        # Generate visualizations
        self._generate_visualizations()

    def _generate_visualizations(self):
        # Use a valid matplotlib style
        plt.style.use('seaborn-v0_8-darkgrid')  # Updated for compatibility
        # Create a figure with multiple subplots
        plt.figure(figsize=(20, 15))
        
        # 1. Move Count Progression
        plt.subplot(2, 2, 1)
        tb_moves = [level.get('move_count', 0) if level.get('move_count') is not None else 0 
                   for level in self.toon_blast_data['game_analysis']['levels']]
        rm_moves = [level.get('move_count', 0) if level.get('move_count') is not None else 0 
                   for level in self.royal_match_data['game_analysis']['levels']]
        plt.plot(range(len(tb_moves)), tb_moves, label='Toon Blast', marker='o')
        plt.plot(range(len(rm_moves)), rm_moves, label='Royal Match', marker='o')
        plt.title('Move Count Progression', fontsize=14)
        plt.xlabel('Level', fontsize=12)
        plt.ylabel('Moves', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True)
        
        # 2. Power Tools Usage
        plt.subplot(2, 2, 2)
        tools_data = {
            'Toon Blast': self.toon_blast_stats.power_tools_usage,
            'Royal Match': self.royal_match_stats.power_tools_usage
        }
        tools_df = pd.DataFrame(tools_data)
        tools_df.plot(kind='bar', ax=plt.gca())
        plt.title('Power Tools Usage Comparison', fontsize=14)
        plt.xlabel('Power Tool', fontsize=12)
        plt.ylabel('Usage Count', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(fontsize=10)
        plt.grid(True)
        
        # 3. Obstacle Distribution
        plt.subplot(2, 2, 3)
        obstacles_data = {
            'Toon Blast': self.toon_blast_stats.obstacle_distribution,
            'Royal Match': self.royal_match_stats.obstacle_distribution
        }
        obstacles_df = pd.DataFrame(obstacles_data)
        obstacles_df.plot(kind='bar', ax=plt.gca())
        plt.title('Obstacle Distribution', fontsize=14)
        plt.xlabel('Obstacle Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(fontsize=10)
        plt.grid(True)
        
        # 4. Difficulty Progression
        plt.subplot(2, 2, 4)
        plt.plot(range(len(self.toon_blast_stats.difficulty_progression)), 
                self.toon_blast_stats.difficulty_progression, 
                label='Toon Blast', marker='o')
        plt.plot(range(len(self.royal_match_stats.difficulty_progression)), 
                self.royal_match_stats.difficulty_progression, 
                label='Royal Match', marker='o')
        plt.title('Difficulty Progression', fontsize=14)
        plt.xlabel('Level', fontsize=12)
        plt.ylabel('Difficulty Score', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('game_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Additional visualizations for deeper analysis
        self._generate_additional_visualizations()

    def _generate_additional_visualizations(self):
        # Create a new figure for additional analysis
        plt.figure(figsize=(20, 10))

        # 1. Unused Moves Distribution
        plt.subplot(1, 2, 1)
        tb_unused = [level.get('unused_moves', 0) if level.get('unused_moves') is not None else 0 
                    for level in self.toon_blast_data['game_analysis']['levels']]
        rm_unused = [level.get('unused_moves', 0) if level.get('unused_moves') is not None else 0 
                    for level in self.royal_match_data['game_analysis']['levels']]
        
        plt.hist([tb_unused, rm_unused], label=['Toon Blast', 'Royal Match'], 
                bins=20, alpha=0.7)
        plt.title('Distribution of Unused Moves', fontsize=14)
        plt.xlabel('Number of Unused Moves', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True)

        # 2. Hint Usage Pattern
        plt.subplot(1, 2, 2)
        tb_hints = [level.get('hint_usage', 0) if level.get('hint_usage') is not None else 0 
                   for level in self.toon_blast_data['game_analysis']['levels']]
        rm_hints = [level.get('hint_usage', 0) if level.get('hint_usage') is not None else 0 
                   for level in self.royal_match_data['game_analysis']['levels']]
        
        plt.plot(range(len(tb_hints)), tb_hints, label='Toon Blast', marker='o')
        plt.plot(range(len(rm_hints)), rm_hints, label='Royal Match', marker='o')
        plt.title('Hint Usage Pattern', fontsize=14)
        plt.xlabel('Level', fontsize=12)
        plt.ylabel('Hints Used', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True)

        plt.tight_layout()
        plt.savefig('game_analysis_additional.png', dpi=300, bbox_inches='tight')
        plt.close()

    def generate_game_objects_md(self):
        """Generate game-objects.md with comprehensive analysis"""
        
        # Helper function to format float values safely
        def format_float(value):
            if pd.isna(value) or np.isinf(value):
                return "N/A"
            return f"{value:.1f}"
        
        # Calculate additional insights
        tb_move_min = min([level.get('move_count', float('inf')) for level in self.toon_blast_data['game_analysis']['levels'] 
                         if level.get('move_count') is not None], default=0)
        tb_move_max = max([level.get('move_count', 0) for level in self.toon_blast_data['game_analysis']['levels'] 
                         if level.get('move_count') is not None], default=0)
        rm_move_min = min([level.get('move_count', float('inf')) for level in self.royal_match_data['game_analysis']['levels'] 
                         if level.get('move_count') is not None], default=0)
        rm_move_max = max([level.get('move_count', 0) for level in self.royal_match_data['game_analysis']['levels'] 
                         if level.get('move_count') is not None], default=0)
        
        content = """# Game Analysis: Toon Blast vs Royal Match

## Overview
This document provides a detailed analysis comparing two popular mobile puzzle games: Toon Blast and Royal Match. The analysis is based on gameplay data from the first 40 levels of each game.

## Game Mechanics Comparison

### Level Design
1. **Move Count**
   - Toon Blast: Average moves per level: {}, Range: {} - {}
   - Royal Match: Average moves per level: {}, Range: {} - {}

2. **Power Tools**
   - Toon Blast: {}
   - Royal Match: {}

3. **Obstacles**
   - Toon Blast: {}
   - Royal Match: {}

### Progression System

1. **Difficulty Curve**
   - Toon Blast shows generally more consistent difficulty progression with fewer extreme spikes
   - Royal Match has more variance in difficulty between levels

2. **Booster System**
   - Toon Blast Boosters: {}
   - Royal Match Boosters: {}

3. **Special Events**
   - Toon Blast Events: {}
   - Royal Match Events: {}, including the unique Butler Gift system

## Key Findings

1. **Level Design Philosophy**
   - Toon Blast offers higher average move counts ({} vs {}), suggesting more forgiving gameplay
   - Royal Match has a wider variety of obstacles, creating more diverse gameplay challenges
   - Power tool distribution shows that Toon Blast emphasizes disco balls and rockets, while Royal Match has a more even distribution across tool types

2. **Player Experience**
   - Toon Blast has higher average unused moves ({}), suggesting easier early levels for player onboarding
   - Royal Match has higher hint usage ({}), potentially indicating more complex puzzles requiring assistance
   - Special events follow different patterns: Toon Blast uses Crown Rush to create engagement, while Royal Match uses Butler Gifts

3. **Monetization Touchpoints**
   - Both games provide opportunities to purchase additional moves
   - Booster unlocks are spaced throughout early levels to introduce players to power-ups
   - Special events like Crown Rush (Toon Blast) and Butler Gifts (Royal Match) create rewards for consecutive wins

## Recommendations

1. **Level Design**
   - **For Toon Blast:** Consider introducing more obstacle variety to increase gameplay diversity
   - **For Royal Match:** Evaluate whether the higher hint usage indicates excessive difficulty in certain levels
   - Both games would benefit from a more gradual difficulty curve with fewer dramatic spikes

2. **Player Engagement**
   - **For Toon Blast:** Implement a system similar to Butler Gifts to reward consecutive level completion
   - **For Royal Match:** Consider adopting the Crown Rush mechanic to create additional engagement loops
   - Both games should optimize distribution of special events to maintain player momentum

3. **Monetization**
   - **For Toon Blast:** More strategic placement of difficult levels where players might need to purchase additional moves
   - **For Royal Match:** Expand on the Butler Gift system as it creates positive reinforcement for continued play
   - Both games should continue to introduce new boosters at key difficulty spikes

## Conclusion
While both games follow similar match-3 puzzle mechanics, they employ different strategies for player retention and monetization. Toon Blast offers more moves and focuses on special events like Crown Rush, while Royal Match has a more diverse obstacle system and uses the Butler Gift to reward consecutive wins. Both games could benefit from adopting successful elements from each other while maintaining their unique identities.
""".format(
            format_float(self.toon_blast_stats.avg_moves), tb_move_min, tb_move_max,
            format_float(self.royal_match_stats.avg_moves), rm_move_min, rm_move_max,
            ', '.join(sorted(self.toon_blast_stats.power_tools_usage.keys())),
            ', '.join(sorted(self.royal_match_stats.power_tools_usage.keys())),
            ', '.join(sorted(self.toon_blast_stats.obstacle_distribution.keys())),
            ', '.join(sorted(self.royal_match_stats.obstacle_distribution.keys())),
            ', '.join(sorted(self.toon_blast_stats.booster_unlocks)),
            ', '.join(sorted(self.royal_match_stats.booster_unlocks)),
            ', '.join(sorted(self.toon_blast_stats.special_events.keys())),
            ', '.join(sorted(self.royal_match_stats.special_events.keys())),
            format_float(self.toon_blast_stats.avg_moves),
            format_float(self.royal_match_stats.avg_moves),
            format_float(self.toon_blast_stats.avg_unused_moves),
            format_float(self.royal_match_stats.avg_hint_usage)
        )

        with open('game-objects.md', 'w') as f:
            f.write(content)

def main():
    analyzer = GameAnalyzer('game-analysis-toon-blast.json', 'game-analysis-royal-match.json')
    analyzer.generate_comparison_report()
    analyzer.generate_game_objects_md()

if __name__ == "__main__":
    main() 