import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

# Set style for all plots
plt.style.use('ggplot')

# Create output directory if it doesn't exist
import os
if not os.path.exists('charts'):
    os.makedirs('charts')

# Colors
royal_match_color = '#8884d8'
toon_blast_color = '#82ca9d'
pie_colors = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8']

#########################################
# 1. Difficulty Curve Visualization
#########################################

# Data
levels = list(range(1, 41))
royal_match_difficulty = [
    1, 1, 1, 2, 2, 2, 2, 3, 2, 3,  # 1-10
    3, 3, 4, 3, 2, 2, 4, 3, 5, 4,  # 11-20
    3, 3, 4, 4, 4, 4, 4, 4, 5, 4,  # 21-30
    4, 3, 3, 5, 3, 4, 4, 3, 5, 5   # 31-40
]

toon_blast_difficulty = [
    1, 1, 2, 2, 2, 2, 2, 3, 2, 3,  # 1-10
    3, 4, 5, 4, 5, 3, 4, 4, 3, 5,  # 11-20
    5, 4, 4, 3, 5, 4, 5, 3, 5, 4,  # 21-30
    2, 4, 3, 3, 4, 4, 4, 3, 4, 4   # 31-40
]

plt.figure(figsize=(12, 6))
plt.plot(levels, royal_match_difficulty, 'o-', color=royal_match_color, linewidth=2, label='Royal Match')
plt.plot(levels, toon_blast_difficulty, 'o-', color=toon_blast_color, linewidth=2, label='Toon Blast')
plt.title('Difficulty Progression (Levels 1-40)', fontsize=16)
plt.xlabel('Level Number', fontsize=12)
plt.ylabel('Difficulty Rating (1-5)', fontsize=12)
plt.xticks(np.arange(0, 41, 5))
plt.yticks(np.arange(0, 6, 1))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/difficulty_progression.png', dpi=300)
plt.close()

#########################################
# 2. Average Difficulty by Segment
#########################################

# Calculate segment averages
segments = ['1-10', '11-20', '21-30', '31-40']
rm_segment_avg = [
    sum(royal_match_difficulty[0:10])/10,
    sum(royal_match_difficulty[10:20])/10,
    sum(royal_match_difficulty[20:30])/10,
    sum(royal_match_difficulty[30:40])/10
]
tb_segment_avg = [
    sum(toon_blast_difficulty[0:10])/10,
    sum(toon_blast_difficulty[10:20])/10,
    sum(toon_blast_difficulty[20:30])/10,
    sum(toon_blast_difficulty[30:40])/10
]

plt.figure(figsize=(10, 6))
bar_width = 0.35
r1 = np.arange(len(segments))
r2 = [x + bar_width for x in r1]

plt.bar(r1, rm_segment_avg, width=bar_width, color=royal_match_color, label='Royal Match')
plt.bar(r2, tb_segment_avg, width=bar_width, color=toon_blast_color, label='Toon Blast')

plt.xlabel('Level Segments', fontsize=12)
plt.ylabel('Average Difficulty (1-5)', fontsize=12)
plt.title('Average Difficulty by 10-Level Segments', fontsize=16)
plt.xticks([r + bar_width/2 for r in range(len(segments))], segments)
plt.yticks(np.arange(0, 6, 1))
plt.legend()
plt.tight_layout()
plt.savefig('charts/difficulty_by_segment.png', dpi=300)
plt.close()

#########################################
# 3. Move Count Comparison
#########################################

# Move count data by game segment
move_count_data = {
    'segment': ['Levels 1-10', 'Levels 11-20', 'Levels 21-30', 'Levels 31-40'],
    'Royal Match': [27.1, 25.0, 24.8, 23.5],
    'Toon Blast': [41.2, 24.5, 28.1, 29.3]
}

df_moves = pd.DataFrame(move_count_data)

plt.figure(figsize=(10, 6))
bar_width = 0.35
r1 = np.arange(len(df_moves['segment']))
r2 = [x + bar_width for x in r1]

plt.bar(r1, df_moves['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
plt.bar(r2, df_moves['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')

plt.xlabel('Level Segments', fontsize=12)
plt.ylabel('Average Move Count', fontsize=12)
plt.title('Average Move Count By Level Segment', fontsize=16)
plt.xticks([r + bar_width/2 for r in range(len(df_moves['segment']))], df_moves['segment'])
plt.legend()
plt.tight_layout()
plt.savefig('charts/move_count_comparison.png', dpi=300)
plt.close()

#########################################
# 4. Power-up Distribution Pie Charts
#########################################

# Royal Match Power Tools
rm_power_tools = {
    'Tool': ['TNT', 'Propeller', 'Rocket', 'Light Ball'],
    'Count': [83, 93, 119, 40]
}

# Toon Blast Power Tools
tb_power_tools = {
    'Tool': ['Bomb', 'Rocket', 'Disco Ball'],
    'Count': [70, 110, 135]
}

# Create a figure with two pie charts side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Royal Match power-up distribution
ax1.pie(rm_power_tools['Count'], labels=rm_power_tools['Tool'], autopct='%1.1f%%', 
        startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'w'})
ax1.set_title('Royal Match: Power-up Distribution', fontsize=16)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Toon Blast power-up distribution
ax2.pie(tb_power_tools['Count'], labels=tb_power_tools['Tool'], autopct='%1.1f%%',
        startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'w'})
ax2.set_title('Toon Blast: Power-up Distribution', fontsize=16)
ax2.axis('equal')

plt.tight_layout()
plt.savefig('charts/power_up_distribution.png', dpi=300)
plt.close()

#########################################
# 5. Obstacle Distribution Bar Chart
#########################################

# Obstacle data
rm_obstacles = {
    'Obstacle': ['Box', 'Grass', 'Plate', 'Mail', 'Egg'],
    'Count': [480, 350, 450, 475, 275]
}

tb_obstacles = {
    'Obstacle': ['Balloon', 'Crate', 'Bubble', 'Carrot', 'Colored-Balloon'],
    'Count': [2100, 440, 400, 630, 560]
}

# Create a figure for Royal Match obstacles
plt.figure(figsize=(10, 6))
plt.bar(rm_obstacles['Obstacle'], rm_obstacles['Count'], color=royal_match_color)
plt.title('Royal Match: Obstacle Distribution', fontsize=16)
plt.xlabel('Obstacle Type', fontsize=12)
plt.ylabel('Total Count', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/royal_match_obstacles.png', dpi=300)
plt.close()

# Create a figure for Toon Blast obstacles
plt.figure(figsize=(10, 6))
plt.bar(tb_obstacles['Obstacle'], tb_obstacles['Count'], color=toon_blast_color)
plt.title('Toon Blast: Obstacle Distribution', fontsize=16)
plt.xlabel('Obstacle Type', fontsize=12)
plt.ylabel('Total Count', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/toon_blast_obstacles.png', dpi=300)
plt.close()

#########################################
# 6. Key Game Metrics Comparison
#########################################

# Key metrics data
key_metrics_data = {
    'Metric': ['Average Moves', 'Average Unused Moves', 'Average Hint Usage', 'New Booster Count'],
    'Royal Match': [25.1, 8.0, 1.2, 5],
    'Toon Blast': [30.7, 9.5, 0.0, 4]
}

df_metrics = pd.DataFrame(key_metrics_data)

plt.figure(figsize=(10, 6))
bar_width = 0.35
r1 = np.arange(len(df_metrics['Metric']))
r2 = [x + bar_width for x in r1]

plt.bar(r1, df_metrics['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
plt.bar(r2, df_metrics['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')

plt.xlabel('Metrics', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Key Game Metrics Comparison', fontsize=16)
plt.xticks([r + bar_width/2 for r in range(len(df_metrics['Metric']))], df_metrics['Metric'], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('charts/key_metrics_comparison.png', dpi=300)
plt.close()

#########################################
# 7. Retention Feature Introduction Timing
#########################################

# Retention feature data
retention_data = {
    'Feature': ['Rating Request', 'New Environment', 'Consecutive Win System', 'Major Difficulty Spike'],
    'Royal Match': [15, 30, 32, 19],
    'Toon Blast': [11, 20, 24, 15]
}

df_retention = pd.DataFrame(retention_data)

plt.figure(figsize=(10, 6))
bar_width = 0.35
r1 = np.arange(len(df_retention['Feature']))
r2 = [x + bar_width for x in r1]

plt.bar(r1, df_retention['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
plt.bar(r2, df_retention['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')

plt.xlabel('Feature', fontsize=12)
plt.ylabel('Level Introduced', fontsize=12)
plt.title('Retention Feature Introduction (Level Number)', fontsize=16)
plt.xticks([r + bar_width/2 for r in range(len(df_retention['Feature']))], df_retention['Feature'], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('charts/retention_features_timing.png', dpi=300)
plt.close()

#########################################
# 8. Combined Dashboard (Summary)
#########################################

plt.figure(figsize=(16, 20))
gs = GridSpec(3, 2, figure=plt.gcf())

# Difficulty Progression
ax1 = plt.subplot(gs[0, 0])
ax1.plot(levels, royal_match_difficulty, 'o-', color=royal_match_color, linewidth=2, markersize=4, label='Royal Match')
ax1.plot(levels, toon_blast_difficulty, 'o-', color=toon_blast_color, linewidth=2, markersize=4, label='Toon Blast')
ax1.set_title('Difficulty Progression', fontsize=14)
ax1.set_xlabel('Level Number', fontsize=10)
ax1.set_ylabel('Difficulty (1-5)', fontsize=10)
ax1.set_xticks(np.arange(0, 41, 10))
ax1.set_yticks(np.arange(0, 6, 1))
ax1.legend(fontsize=9)
ax1.grid(True)

# Move Count Comparison
ax2 = plt.subplot(gs[0, 1])
r1 = np.arange(len(df_moves['segment']))
r2 = [x + bar_width for x in r1]
ax2.bar(r1, df_moves['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
ax2.bar(r2, df_moves['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')
ax2.set_xlabel('Level Segments', fontsize=10)
ax2.set_ylabel('Average Move Count', fontsize=10)
ax2.set_title('Average Move Count By Segment', fontsize=14)
ax2.set_xticks([r + bar_width/2 for r in range(len(df_moves['segment']))])
ax2.set_xticklabels(df_moves['segment'], rotation=45, fontsize=8)
ax2.legend(fontsize=9)

# Key Metrics Comparison
ax3 = plt.subplot(gs[1, 0])
r1 = np.arange(len(df_metrics['Metric']))
r2 = [x + bar_width for x in r1]
ax3.bar(r1, df_metrics['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
ax3.bar(r2, df_metrics['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')
ax3.set_xlabel('Metrics', fontsize=10)
ax3.set_ylabel('Value', fontsize=10)
ax3.set_title('Key Game Metrics', fontsize=14)
ax3.set_xticks([r + bar_width/2 for r in range(len(df_metrics['Metric']))])
ax3.set_xticklabels(df_metrics['Metric'], rotation=45, fontsize=8)
ax3.legend(fontsize=9)

# Retention Features
ax4 = plt.subplot(gs[1, 1])
r1 = np.arange(len(df_retention['Feature']))
r2 = [x + bar_width for x in r1]
ax4.bar(r1, df_retention['Royal Match'], width=bar_width, color=royal_match_color, label='Royal Match')
ax4.bar(r2, df_retention['Toon Blast'], width=bar_width, color=toon_blast_color, label='Toon Blast')
ax4.set_xlabel('Feature', fontsize=10)
ax4.set_ylabel('Level Introduced', fontsize=10)
ax4.set_title('Retention Feature Timing', fontsize=14)
ax4.set_xticks([r + bar_width/2 for r in range(len(df_retention['Feature']))])
ax4.set_xticklabels(df_retention['Feature'], rotation=45, fontsize=8)
ax4.legend(fontsize=9)

# Royal Match Power-Up Distribution
ax5 = plt.subplot(gs[2, 0])
ax5.pie(rm_power_tools['Count'], labels=rm_power_tools['Tool'], autopct='%1.1f%%', 
        startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'w'})
ax5.set_title('Royal Match: Power-up Distribution', fontsize=14)
ax5.axis('equal')

# Toon Blast Power-Up Distribution
ax6 = plt.subplot(gs[2, 1])
ax6.pie(tb_power_tools['Count'], labels=tb_power_tools['Tool'], autopct='%1.1f%%',
        startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'w'})
ax6.set_title('Toon Blast: Power-up Distribution', fontsize=14)
ax6.axis('equal')

plt.suptitle('Royal Match vs. Toon Blast: Comparative Analysis', fontsize=18, y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('charts/game_analysis_dashboard.png', dpi=300)
plt.close()

print("All charts have been saved to the 'charts' directory.")
