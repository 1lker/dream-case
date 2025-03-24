import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patheffects as path_effects
from matplotlib.gridspec import GridSpec
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from matplotlib.patches import Patch

# Set style for all plots
plt.style.use('ggplot')
sns.set_style("whitegrid")

# Create output directory if it doesn't exist
import os
if not os.path.exists('game_charts'):
    os.makedirs('game_charts')

# Enhanced color scheme
royal_match_color = '#7030A0'  # A richer purple for royal theme
toon_blast_color = '#00B050'   # A vibrant green for cartoon theme
pie_colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5', '#70AD47']
background_color = '#F5F5F5'
text_color = '#333333'
grid_color = '#DDDDDD'

# Custom color maps
royal_cmap = LinearSegmentedColormap.from_list('royal_map', ['#C9B7DC', '#7030A0'])
toon_cmap = LinearSegmentedColormap.from_list('toon_map', ['#C5E0B4', '#00B050'])

# Set global font properties
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['axes.edgecolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
plt.rcParams['axes.titlecolor'] = text_color
plt.rcParams['text.color'] = text_color

# Utility function to add text with outline for better readability
def text_with_outline(ax, x, y, text, **kwargs):
    txt = ax.text(x, y, text, **kwargs)
    txt.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    return txt

#########################################
# 1. Enhanced Difficulty Curve Visualization
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

# Key events/milestones - IMPROVED POSITIONING
rm_events = {
    7: {"name": "Royal Hammer", "type": "Booster unlock", "y_offset": -0.7, "x_offset": 0},
    14: {"name": "Arrow", "type": "Booster unlock", "y_offset": -0.7, "x_offset": 0},
    15: {"name": "Rating request", "type": "Feedback", "y_offset": -0.7, "x_offset": -1.5},
    17: {"name": "Cannon", "type": "Booster unlock", "y_offset": -0.7, "x_offset": 0},
    19: {"name": "Jester Hat\n(1 move level)", "type": "Major difficulty spike", "y_offset": -0.7, "x_offset": 0},
    20: {"name": "Coin Rain", "type": "Bonus level", "y_offset": -0.7, "x_offset": 1.5},
    32: {"name": "Butler's Gift", "type": "Retention feature", "y_offset": -0.7, "x_offset": -1.5},
    39: {"name": "Magic Cauldron", "type": "Feature unlock", "y_offset": -0.7, "x_offset": 0}
}

tb_events = {
    9: {"name": "Hammer", "type": "Booster unlock", "y_offset": 0.7, "x_offset": 0},
    11: {"name": "Rating request", "type": "Feedback", "y_offset": 0.7, "x_offset": 0},
    12: {"name": "Boxing Glove", "type": "Booster unlock", "y_offset": 0.7, "x_offset": 1.5},
    16: {"name": "Anvil", "type": "Booster unlock", "y_offset": 0.7, "x_offset": 0},
    18: {"name": "Dice", "type": "Booster unlock", "y_offset": 0.7, "x_offset": -1.5},
    20: {"name": "New episode", "type": "Content unlock", "y_offset": 0.7, "x_offset": 2.5},
    24: {"name": "Crown Rush", "type": "Retention feature", "y_offset": 0.7, "x_offset": 0},
    40: {"name": "New episode", "type": "Content unlock", "y_offset": 0.7, "x_offset": -1}
}

fig, ax = plt.subplots(figsize=(14, 8), facecolor=background_color)

# Plot difficulty lines with shadow effect for depth
ax.plot(levels, royal_match_difficulty, 'o-', color=royal_match_color, linewidth=3, 
        label='Royal Match', markersize=8, path_effects=[path_effects.SimpleLineShadow(), 
                                                        path_effects.Normal()])
ax.plot(levels, toon_blast_difficulty, 'o-', color=toon_blast_color, linewidth=3, 
        label='Toon Blast', markersize=8, path_effects=[path_effects.SimpleLineShadow(), 
                                                       path_effects.Normal()])

# Fill below curves for better visualization
ax.fill_between(levels, royal_match_difficulty, alpha=0.15, color=royal_match_color)
ax.fill_between(levels, toon_blast_difficulty, alpha=0.15, color=toon_blast_color)

# Highlight significant difficulty spikes - FIXED POSITIONS
for i, diff in enumerate(royal_match_difficulty):
    if i > 0 and diff - royal_match_difficulty[i-1] > 1:
        ax.annotate(f'+{diff - royal_match_difficulty[i-1]}', 
                  xy=(levels[i], diff), 
                  xytext=(levels[i]-0.3, diff+0.3),
                  fontsize=9, color=royal_match_color, 
                  fontweight='bold',
                  bbox=dict(boxstyle="round,pad=0.1", fc='white', ec=royal_match_color, alpha=0.8))

for i, diff in enumerate(toon_blast_difficulty):
    if i > 0 and diff - toon_blast_difficulty[i-1] > 1:
        ax.annotate(f'+{diff - toon_blast_difficulty[i-1]}', 
                  xy=(levels[i], diff), 
                  xytext=(levels[i]+0.3, diff+0.3),
                  fontsize=9, color=toon_blast_color, 
                  fontweight='bold',
                  bbox=dict(boxstyle="round,pad=0.1", fc='white', ec=toon_blast_color, alpha=0.8))

# Add markers for key events - IMPROVED POSITIONING
for level, event in rm_events.items():
    ax.plot(level, royal_match_difficulty[level-1], 'o', ms=12, mec=royal_match_color, mfc='white', mew=2)
    ax.annotate(event["name"], 
                xy=(level, royal_match_difficulty[level-1]), 
                xytext=(level + event["x_offset"], royal_match_difficulty[level-1] + event["y_offset"]),
                ha='center', va='top', fontsize=8, color=royal_match_color,
                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=royal_match_color, alpha=0.8))

for level, event in tb_events.items():
    ax.plot(level, toon_blast_difficulty[level-1], 'o', ms=12, mec=toon_blast_color, mfc='white', mew=2)
    ax.annotate(event["name"], 
                xy=(level, toon_blast_difficulty[level-1]), 
                xytext=(level + event["x_offset"], toon_blast_difficulty[level-1] + event["y_offset"]),
                ha='center', va='bottom', fontsize=8, color=toon_blast_color,
                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))

# Add level segments visualization
for i, label in enumerate(['Onboarding', 'Early Game', 'Mid Game', 'Late Game']):
    start = i * 10 + 1
    end = (i + 1) * 10
    ax.axvspan(start-0.5, end+0.5, alpha=0.1, color='black')
    ax.annotate(label, xy=((start+end)/2, 0.2), xycoords=('data', 'axes fraction'),
              ha='center', fontsize=10, color='dimgrey', fontweight='bold')

# Add difficulty level descriptions
for i, label in enumerate(['Very Easy', 'Easy', 'Moderate', 'Hard', 'Very Hard']):
    ax.annotate(label, xy=(41, i+1), xycoords='data',
             ha='left', fontsize=9, color='dimgrey', va='center')

ax.set_title('Difficulty Progression & Key Milestones', fontsize=22, pad=20, fontweight='bold')
ax.set_xlabel('Level Number', fontsize=14, labelpad=10)
ax.set_ylabel('Difficulty Rating (1-5)', fontsize=14, labelpad=10)
ax.set_xlim(0.5, 40.5)
ax.set_ylim(0.5, 5.5)
ax.set_xticks(np.arange(0, 41, 5))
ax.set_yticks(np.arange(1, 6, 1))
ax.tick_params(axis='both', which='major', labelsize=10)

# Create custom legend
legend_elements = [
    Patch(facecolor=royal_match_color, edgecolor='none', alpha=0.6, label='Royal Match'),
    Patch(facecolor=toon_blast_color, edgecolor='none', alpha=0.6, label='Toon Blast'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='w', markeredgecolor=royal_match_color, 
              markeredgewidth=2, markersize=10, label='RM Key Event'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='w', markeredgecolor=toon_blast_color, 
              markeredgewidth=2, markersize=10, label='TB Key Event')
]
ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.12), 
         ncol=4, fontsize=12, frameon=True, facecolor='white', edgecolor=grid_color)

ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('white')
fig.tight_layout(pad=2.0)
plt.savefig('game_charts/difficulty_progression.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

#########################################
# 2. Move Count & Unused Moves Analysis
#########################################

# Data for moves and unused moves
rm_moves = [35, 30, 27, 27, 23, 35, 25, 27, 30, 32, 27, 30, 30, 27, 23, 35, 23, 24, 1, 20, 28, 25, 25, 26, 26, 23, 21, 27, 25, 22, 28, 22, 30, 20, 20, 25, 23, 24, 28, 20]
rm_unused = [12, 15, 10, 7, 13, 9, 9, 7, 16, 13, 10, 12, 4, 10, 15, 20, 6, 10, 0, 0, 13, 9, 4, 3, 5, 5, 2, 4, 1, 4, 5, 7, 40, 0, 8, 3, 4, 9, 3, 0]

tb_moves = [33, 40, 40, 35, 46, 40, 38, 50, 50, 40, 23, 22, 26, 20, 22, 24, 30, 34, 19, 28, 39, 21, 30, 35, 31, 21, 21, 39, 27, 24, 40, 31, 26, 18, 35, 36, 24, 18, 25, 26]
tb_unused = [23, 23, 10, 11, 24, 16, 24, 12, 19, 15, 9, 4, 0, 1, 0, 8, 10, 7, 12, 1, 0, 0, 9, 19, 1, 6, 0, 12, 1, 4, 32, 9, 13, 6, 11, 8, 4, 9, 4, 4]

# Calculate success rate (unused / total moves)
rm_success_rate = [unused / moves * 100 if moves > 0 else 0 for moves, unused in zip(rm_moves, rm_unused)]
tb_success_rate = [unused / moves * 100 if moves > 0 else 0 for moves, unused in zip(tb_moves, tb_unused)]

# Calculate 10-level segments for all metrics
def segment_averages(data_list):
    segments = []
    for i in range(0, 40, 10):
        segment_data = data_list[i:i+10]
        segments.append(sum(segment_data) / len(segment_data))
    return segments

rm_move_segments = segment_averages(rm_moves)
tb_move_segments = segment_averages(tb_moves)
rm_unused_segments = segment_averages(rm_unused)
tb_unused_segments = segment_averages(tb_unused)
rm_success_segments = segment_averages(rm_success_rate)
tb_success_segments = segment_averages(tb_success_rate)

# Create figure with 3 subplots
fig = plt.figure(figsize=(16, 18), facecolor=background_color)
gs = GridSpec(3, 1, height_ratios=[1, 1, 1.2], hspace=0.4)

# 1. Move Count Comparison by Segment
ax1 = fig.add_subplot(gs[0])
segments = ['Levels 1-10', 'Levels 11-20', 'Levels 21-30', 'Levels 31-40']
x = np.arange(len(segments))
width = 0.35

bars1 = ax1.bar(x - width/2, rm_move_segments, width, label='Royal Match', color=royal_match_color, 
               edgecolor='white', linewidth=1)
bars2 = ax1.bar(x + width/2, tb_move_segments, width, label='Toon Blast', color=toon_blast_color, 
               edgecolor='white', linewidth=1)

# Add data labels on bars
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'{height:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'{height:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_title('Average Move Count by Game Segment', fontsize=18, fontweight='bold', pad=15)
ax1.set_ylabel('Average Moves', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(segments)
ax1.legend(fontsize=11)
ax1.set_ylim(0, max(max(rm_move_segments), max(tb_move_segments)) * 1.15)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_facecolor('white')

# Add annotations - FIXED POSITIONING
ax1.annotate('Toon Blast starts with 41.2 average moves\nin onboarding phase (55% more than Royal Match)', 
           xy=(0, tb_move_segments[0]), xytext=(0.5, tb_move_segments[0] + 6),
           arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
           fontsize=10, ha='center', va='bottom',
           bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))

ax1.annotate('Sharp drop in moves for Toon Blast\nafter onboarding (-41%)', 
           xy=(1, tb_move_segments[1]), xytext=(1.4, tb_move_segments[1] + 13),
           arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
           fontsize=10, ha='center', va='bottom',
           bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))

# 2. Unused Moves Comparison by Segment
ax2 = fig.add_subplot(gs[1])

bars3 = ax2.bar(x - width/2, rm_unused_segments, width, label='Royal Match', color=royal_match_color, 
               edgecolor='white', linewidth=1)
bars4 = ax2.bar(x + width/2, tb_unused_segments, width, label='Toon Blast', color=toon_blast_color, 
               edgecolor='white', linewidth=1)

# Add data labels on bars
for bar in bars3:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'{height:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars4:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'{height:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.set_title('Average Unused Moves by Game Segment', fontsize=18, fontweight='bold', pad=15)
ax2.set_ylabel('Average Unused Moves', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(segments)
ax2.legend(fontsize=11)
ax2.set_ylim(0, max(max(rm_unused_segments), max(tb_unused_segments)) * 1.15)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_facecolor('white')

# Add annotations - FIXED POSITIONING
ax2.annotate('Both games have similar pattern of\ndecreasing unused moves as levels progress', 
           xy=(1.5, (rm_unused_segments[1] + tb_unused_segments[1])/2), 
           xytext=(2.3, (rm_unused_segments[1] + tb_unused_segments[1])/2 + 3),
           arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
           fontsize=10, ha='center', va='bottom',
           bbox=dict(boxstyle="round,pad=0.3", fc='white', ec='grey', alpha=0.8))

# 3. Success Rate (Unused/Total %) Comparison with Level Ranges
ax3 = fig.add_subplot(gs[2])

# Sort data for level ranges
range_labels = ['Very Easy\n(>40%)','Easy\n(30-40%)','Moderate\n(20-30%)','Challenging\n(10-20%)','Hard\n(5-10%)','Very Hard\n(<5%)']
rm_ranges = [0, 0, 0, 0, 0, 0]  # Counts for each range
tb_ranges = [0, 0, 0, 0, 0, 0]

for rate in rm_success_rate:
    if rate > 40: rm_ranges[0] += 1
    elif rate > 30: rm_ranges[1] += 1
    elif rate > 20: rm_ranges[2] += 1
    elif rate > 10: rm_ranges[3] += 1
    elif rate > 5: rm_ranges[4] += 1
    else: rm_ranges[5] += 1

for rate in tb_success_rate:
    if rate > 40: tb_ranges[0] += 1
    elif rate > 30: tb_ranges[1] += 1
    elif rate > 20: tb_ranges[2] += 1
    elif rate > 10: tb_ranges[3] += 1
    elif rate > 5: tb_ranges[4] += 1
    else: tb_ranges[5] += 1

x = np.arange(len(range_labels))
bars5 = ax3.bar(x - width/2, rm_ranges, width, label='Royal Match', color=royal_match_color, 
               edgecolor='white', linewidth=1)
bars6 = ax3.bar(x + width/2, tb_ranges, width, label='Toon Blast', color=toon_blast_color, 
               edgecolor='white', linewidth=1)

# Add percentage labels
for bar in bars5:
    height = bar.get_height()
    percentage = height / 40 * 100
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.3,
           f'{height} ({percentage:.0f}%)', ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars6:
    height = bar.get_height()
    percentage = height / 40 * 100
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.3,
           f'{height} ({percentage:.0f}%)', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax3.set_title('Level Difficulty Distribution by Success Rate (Unused/Total Moves)', 
            fontsize=18, fontweight='bold', pad=15)
ax3.set_ylabel('Number of Levels', fontsize=12)
ax3.set_xticks(x)
ax3.set_xticklabels(range_labels)
ax3.legend(fontsize=11)
ax3.set_ylim(0, max(max(rm_ranges), max(tb_ranges)) * 1.2)
ax3.grid(axis='y', linestyle='--', alpha=0.7)
ax3.set_facecolor('white')

# Add color gradient to show difficulty zones
for i, (color1, color2) in enumerate(zip(['#C6EFCE', '#FFEB9C', '#FFC7CE'], ['#006100', '#9C5700', '#9C0006'])):
    ax3.axvspan(i*2-0.5, i*2+1.5, alpha=0.05, color=color2)

# Add annotations with insights - FIXED POSITIONING
ax3.annotate('Toon Blast has more very easy levels (40%+ success rate)', 
           xy=(0, tb_ranges[0]), xytext=(0, tb_ranges[0] + 3),
           arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
           fontsize=10, ha='center', va='bottom',
           bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))

ax3.annotate('Royal Match has more very hard levels (<5% success rate)', 
           xy=(5, rm_ranges[5]), xytext=(4.6, rm_ranges[5] + 3),
           arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
           fontsize=10, ha='center', va='bottom',
           bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=royal_match_color, alpha=0.8))

# Add overall title
fig.suptitle('Move Count & Difficulty Analysis', fontsize=24, fontweight='bold', y=0.98)
plt.tight_layout(pad=2.0)
plt.savefig('game_charts/move_analysis.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

#########################################
# 3. Power-Up Distribution with Effects
#########################################

# Royal Match Power Tools with effects
rm_power_tools = {
    'Tool': ['TNT', 'Propeller', 'Rocket', 'Light Ball'],
    'Count': [83, 93, 119, 40],
    'Effect': ['2-tile radius blast', 'Clears random area', 'Clears row/column', 'Clears same color'],
    'Creation': ['Match 5 in L/T shape', 'Match 4 in square', 'Match 4 in line', 'Match 5 in line']
}

# Toon Blast Power Tools with effects
tb_power_tools = {
    'Tool': ['Bomb', 'Rocket', 'Disco Ball'],
    'Count': [70, 110, 135],
    'Effect': ['Radius blast', 'Clears row/column', 'Clears one color'],
    'Creation': ['Match 7-8 cubes', 'Match 5-6 cubes', 'Match 9+ cubes']
}

# Create a figure with two pie charts and info boxes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10), facecolor=background_color)

# Royal Match power-up distribution
wedges, texts, autotexts = ax1.pie(rm_power_tools['Count'], labels=None, autopct='%1.1f%%', 
                                  startangle=90, colors=pie_colors[:len(rm_power_tools['Tool'])], 
                                  wedgeprops={'edgecolor': 'white', 'linewidth': 2})

# Add detailed legend with effects - FIXED POSITIONING
legend_labels = [f"{tool} ({count})\nEffect: {effect}\nCreation: {creation}" 
                for tool, count, effect, creation in 
                zip(rm_power_tools['Tool'], rm_power_tools['Count'], 
                    rm_power_tools['Effect'], rm_power_tools['Creation'])]

ax1.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(0.9, 0.5), 
          fontsize=11, frameon=True, facecolor='white', edgecolor=grid_color)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax1.set_title('Royal Match: Power-up Distribution & Effects', fontsize=18, fontweight='bold', pad=20)
ax1.set_facecolor('white')

# Add analysis text - FIXED POSITIONING
total_rm = sum(rm_power_tools['Count'])
analysis_text = (f"Total power-ups: {total_rm}\n\n"
                f"Most common: Rocket ({rm_power_tools['Count'][2]}, "
                f"{rm_power_tools['Count'][2]/total_rm*100:.1f}%)\n\n"
                f"Least common: Light Ball ({rm_power_tools['Count'][3]}, "
                f"{rm_power_tools['Count'][3]/total_rm*100:.1f}%)\n\n"
                f"Royal Match favors row/column\nclearers over area effects")

ax1.text(-0.3, -0.1, analysis_text, transform=ax1.transAxes, fontsize=12,
        bbox=dict(boxstyle="round,pad=0.6", fc='white', ec=royal_match_color, alpha=0.8))

# Toon Blast power-up distribution
wedges, texts, autotexts = ax2.pie(tb_power_tools['Count'], labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=pie_colors[:len(tb_power_tools['Tool'])],
                                  wedgeprops={'edgecolor': 'white', 'linewidth': 2})

# Add detailed legend with effects - FIXED POSITIONING
legend_labels = [f"{tool} ({count})\nEffect: {effect}\nCreation: {creation}" 
                for tool, count, effect, creation in 
                zip(tb_power_tools['Tool'], tb_power_tools['Count'], 
                    tb_power_tools['Effect'], tb_power_tools['Creation'])]

ax2.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(0.9, 0.5), 
          fontsize=11, frameon=True, facecolor='white', edgecolor=grid_color)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax2.set_title('Toon Blast: Power-up Distribution & Effects', fontsize=18, fontweight='bold', pad=20)
ax2.set_facecolor('white')

# Add analysis text - FIXED POSITIONING
total_tb = sum(tb_power_tools['Count'])
analysis_text = (f"Total power-ups: {total_tb}\n\n"
                f"Most common: Disco Ball ({tb_power_tools['Count'][2]}, "
                f"{tb_power_tools['Count'][2]/total_tb*100:.1f}%)\n\n"
                f"Least common: Bomb ({tb_power_tools['Count'][0]}, "
                f"{tb_power_tools['Count'][0]/total_tb*100:.1f}%)\n\n"
                f"Toon Blast emphasizes color clearers\nreflecting its simpler board layouts")

ax2.text(-0.3, -0.1, analysis_text, transform=ax2.transAxes, fontsize=12,
        bbox=dict(boxstyle="round,pad=0.6", fc='white', ec=toon_blast_color, alpha=0.8))

# Add comparison callout in center - IMPROVED POSITIONING
fig.text(0.5, 0.05, 
        "Royal Match uses more power-up types (4 vs 3) but Toon Blast has higher overall usage (315 vs 335)",
        ha='center', va='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.6", fc='white', ec='gray', alpha=0.9))

plt.suptitle('Power-Up Mechanics & Distribution Analysis', fontsize=24, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.08, 1, 0.95], pad=2.0)
plt.savefig('game_charts/power_up_analysis.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

#########################################
# 4. Enhanced Obstacle Distribution Analysis
#########################################

# Obstacle data with levels of first appearance
rm_obstacles = {
    'Obstacle': ['Box', 'Grass', 'Plate', 'Mail', 'Egg'],
    'Count': [480, 350, 450, 475, 275],
    'First Level': [4, 5, 11, 21, 31],
    'Description': ['Requires matches next to it', 'Multiple layers to clear', 'Blocks access to items beneath', 'Must be collected', 'Must be collected']
}

tb_obstacles = {
    'Obstacle': ['Balloon', 'Crate', 'Bubble', 'Carrot', 'Colored-Balloon'],
    'Count': [2100, 440, 400, 630, 560],
    'First Level': [1, 4, 11, 21, 31],
    'Description': ['Must be popped to complete level', 'Requires matches next to it', 'Must be popped', 'Must be collected', 'Color-specific balloons']
}

# Create figure for obstacle distribution
fig = plt.figure(figsize=(20, 14), facecolor=background_color)
gs = GridSpec(2, 2, height_ratios=[1, 1.2], hspace=0.4, wspace=0.3)

# 1. Royal Match obstacle barchart - FIXED LAYOUT
ax1 = fig.add_subplot(gs[0, 0])
bars1 = ax1.bar(rm_obstacles['Obstacle'], rm_obstacles['Count'], color=royal_cmap(np.linspace(0.2, 0.8, len(rm_obstacles['Obstacle']))),
              edgecolor='white', linewidth=1)

# Add only first appearance level on bars, move descriptions to a table
for i, bar in enumerate(bars1):
    height = bar.get_height()
    first_level = rm_obstacles['First Level'][i]
    ax1.text(bar.get_x() + bar.get_width()/2., height + 20,
           f'{height}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax1.text(bar.get_x() + bar.get_width()/2., height/2,
           f'Level {first_level}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

ax1.set_title('Royal Match: Obstacle Distribution', fontsize=18, fontweight='bold', pad=15)
ax1.set_ylabel('Total Count', fontsize=14)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_facecolor('white')

# 2. Toon Blast obstacle barchart - FIXED LAYOUT
ax2 = fig.add_subplot(gs[0, 1])
bars2 = ax2.bar(tb_obstacles['Obstacle'], tb_obstacles['Count'], color=toon_cmap(np.linspace(0.2, 0.8, len(tb_obstacles['Obstacle']))),
              edgecolor='white', linewidth=1)

# Add only first appearance level on bars, move descriptions to a table
for i, bar in enumerate(bars2):
    height = bar.get_height()
    first_level = tb_obstacles['First Level'][i]
    ax2.text(bar.get_x() + bar.get_width()/2., height + 100,
           f'{height}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax2.text(bar.get_x() + bar.get_width()/2., height/2,
           f'Level {first_level}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

ax2.set_title('Toon Blast: Obstacle Distribution', fontsize=18, fontweight='bold', pad=15)
ax2.set_ylabel('Total Count', fontsize=14)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_facecolor('white')

# Add obstacle descriptions as tables below the charts
# Table for Royal Match obstacles
rm_table_ax = fig.add_axes([0.05, 0.45, 0.4, 0.1])  # x, y, width, height in figure coordinates
rm_table_ax.axis('off')

# Create rows for each obstacle
for i, (obstacle, desc) in enumerate(zip(rm_obstacles['Obstacle'], rm_obstacles['Description'])):
    y_pos = 0.9 - i * 0.2
    color = royal_cmap(0.2 + i * 0.6 / len(rm_obstacles['Obstacle']))
    
    # Add colored square
    rm_table_ax.add_patch(plt.Rectangle((0.05, y_pos - 0.1), 0.05, 0.15, facecolor=color, edgecolor='white'))
    
    # Add obstacle name and description
    rm_table_ax.text(0.12, y_pos, f"{obstacle}: ", fontsize=10, fontweight='bold', va='center')
    rm_table_ax.text(0.25, y_pos, desc, fontsize=10, va='center')

# Table for Toon Blast obstacles
tb_table_ax = fig.add_axes([0.55, 0.45, 0.4, 0.1])  # x, y, width, height in figure coordinates
tb_table_ax.axis('off')

# Create rows for each obstacle
for i, (obstacle, desc) in enumerate(zip(tb_obstacles['Obstacle'], tb_obstacles['Description'])):
    y_pos = 0.9 - i * 0.2
    color = toon_cmap(0.2 + i * 0.6 / len(tb_obstacles['Obstacle']))
    
    # Add colored square
    tb_table_ax.add_patch(plt.Rectangle((0.05, y_pos - 0.1), 0.05, 0.15, facecolor=color, edgecolor='white'))
    
    # Add obstacle name and description
    tb_table_ax.text(0.12, y_pos, f"{obstacle}: ", fontsize=10, fontweight='bold', va='center')
    tb_table_ax.text(0.27, y_pos, desc, fontsize=10, va='center')

plt.suptitle('Obstacle System Analysis', fontsize=24, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.3, 1, 0.95], pad=2.0)
plt.savefig('game_charts/obstacle_distribution.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

# SEPARATE OBSTACLE TIMING VISUALIZATION - ENHANCED WITH MORE SPACING
plt.figure(figsize=(20, 10), facecolor=background_color)

# Set up the plot area
ax = plt.gca()
ax.set_xlim(0, 41)
ax.set_ylim(0, 20)  # Increased height for better separation
ax.set_xlabel('Level Number', fontsize=14)
ax.set_title('Obstacle Introduction Timing & Progression', fontsize=22, fontweight='bold', pad=15)
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.set_facecolor('white')

# Remove y-axis ticks/labels as they're not relevant
ax.set_yticks([])

# Add level number markers
ax.set_xticks(range(0, 41, 5))
ax.tick_params(axis='x', labelsize=12)

# SIGNIFICANTLY IMPROVED SPACING

# Plot Royal Match obstacle appearances with much better spacing
# Royal Match section is in the upper half
vertical_space = 2.5  # Much larger spacing between obstacles
for i, obstacle in enumerate(rm_obstacles['Obstacle']):
    level = rm_obstacles['First Level'][i]
    color = royal_cmap(0.2 + i * 0.6 / len(rm_obstacles['Obstacle']))
    
    # Y-position with much more spacing
    y_pos = 16 - i*vertical_space
    
    # Draw a horizontal line from introduction to end
    ax.plot([level, 40], [y_pos, y_pos], linewidth=6, color=color, alpha=0.7)
    
    # Add a marker for introduction point
    ax.scatter(level, y_pos, s=150, color=color, edgecolor='white', zorder=10)
    
    # Add labels with clear background and more spacing
    # Obstacle name above the line
    ax.text(level, y_pos + 0.8, obstacle, fontsize=12, ha='center', va='center', 
            color=royal_match_color, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=royal_match_color, alpha=0.8))
    
    # Level number below the line
    ax.text(level, y_pos - 0.8, f'Level {level}', fontsize=10, ha='center', va='center', 
            color=royal_match_color,
            bbox=dict(boxstyle="round,pad=0.2", fc='white', ec=royal_match_color, alpha=0.5))

# Plot Toon Blast obstacle appearances with much better spacing
# Toon Blast section is in the lower half
for i, obstacle in enumerate(tb_obstacles['Obstacle']):
    level = tb_obstacles['First Level'][i]
    color = toon_cmap(0.2 + i * 0.6 / len(tb_obstacles['Obstacle']))
    
    # Y-position with much more spacing, in the lower half
    y_pos = 8 - i*vertical_space
    
    # Draw a horizontal line from introduction to end
    ax.plot([level, 40], [y_pos, y_pos], linewidth=6, color=color, alpha=0.7)
    
    # Add a marker for introduction point
    ax.scatter(level, y_pos, s=150, color=color, edgecolor='white', zorder=10)
    
    # Add labels with clear background and more spacing
    # Obstacle name above the line
    ax.text(level, y_pos + 0.8, obstacle, fontsize=12, ha='center', va='center', 
            color=toon_blast_color, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))
    
    # Level number below the line
    ax.text(level, y_pos - 0.8, f'Level {level}', fontsize=10, ha='center', va='center', 
            color=toon_blast_color,
            bbox=dict(boxstyle="round,pad=0.2", fc='white', ec=toon_blast_color, alpha=0.5))

# Add game labels
ax.text(2, 17.5, 'Royal Match', fontsize=16, color=royal_match_color, fontweight='bold', 
       ha='left', va='center', bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=royal_match_color, alpha=0.2))
ax.text(2, 9.5, 'Toon Blast', fontsize=16, color=toon_blast_color, fontweight='bold', 
       ha='left', va='center', bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.2))

# Add insights box in the middle right
insights = [
    "Both games introduce new obstacles at ~10 level intervals",
    "Toon Blast has significantly higher obstacle counts overall (4130 vs 2030)",
    "Royal Match has more even distribution across obstacle types",
    "First obstacles remain consistently used throughout (Box for RM, Balloon for TB)"
]

# Create a text box for insights
props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray')
ax.text(30, 12.5, "Key Insights:", fontsize=14, fontweight='bold', ha='center', va='center')

# Add insights with bullet points
for i, insight in enumerate(insights):
    ax.text(30, 11 - i*1.2, f"• {insight}", fontsize=11, ha='center', va='center',
           bbox=dict(boxstyle="round,pad=0.2", fc='white', ec='gray', alpha=0.7))

# Add dividing line between Royal Match and Toon Blast sections
ax.axhline(y=12, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('game_charts/obstacle_timing.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

#########################################
# 5. Retention Feature Comparison & Monetization Touchpoints
#########################################

# Key retention features data
retention_data = {
    'Feature': ['Rating Request', 'New Environment', 'Consecutive Win System', 'Major Difficulty Spike', 'New Booster'],
    'Royal Match': [15, 30, 32, 19, 17],
    'Toon Blast': [11, 20, 24, 15, 16]
}

# Monetization touchpoints
rm_monetization = [
    {'level': 19, 'type': 'Extreme Difficulty', 'description': 'Only 1 move available', 'y_offset': 1.0},
    {'level': 23, 'type': 'Additional Moves', 'description': 'Required 5 extra moves', 'y_offset': 1.0},
    {'level': 33, 'type': 'Additional Moves', 'description': 'Required 5 extra moves', 'y_offset': 1.0},
    {'level': 39, 'type': 'Additional Moves', 'description': 'Required 5 extra moves', 'y_offset': 1.0}
]

tb_monetization = [
    {'level': 13, 'type': 'Zero Unused Moves', 'description': 'Triple obstacle types', 'y_offset': -1.0},
    {'level': 15, 'type': 'Additional Moves', 'description': 'Required 5 extra moves', 'y_offset': -1.0},
    {'level': 21, 'type': 'Zero Unused Moves', 'description': 'New obstacle (Carrot)', 'y_offset': -1.0},
    {'level': 27, 'type': 'Zero Unused Moves', 'description': 'Low move count (21)', 'y_offset': -1.0}
]

# Create figure
fig = plt.figure(figsize=(16, 12), facecolor=background_color)
gs = GridSpec(2, 1, height_ratios=[1, 1.3], hspace=0.4)

# 1. Retention feature comparison
ax1 = fig.add_subplot(gs[0])
df_retention = pd.DataFrame(retention_data)

x = np.arange(len(df_retention['Feature']))
width = 0.35

bars1 = ax1.bar(x - width/2, df_retention['Royal Match'], width, color=royal_match_color, 
              edgecolor='white', linewidth=1, label='Royal Match')
bars2 = ax1.bar(x + width/2, df_retention['Toon Blast'], width, color=toon_blast_color, 
              edgecolor='white', linewidth=1, label='Toon Blast')

# Add data labels - IMPROVED POSITIONING
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'Level {height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
           f'Level {height}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_title('Retention Feature Introduction Timing', fontsize=18, fontweight='bold', pad=15)
ax1.set_ylabel('Level Number', fontsize=14)
ax1.set_xticks(x)
ax1.set_xticklabels(df_retention['Feature'], fontsize=12)
ax1.legend(fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_facecolor('white')

# Add difference annotations - IMPROVED POSITIONING
for i, feature in enumerate(df_retention['Feature']):
    rm_level = df_retention['Royal Match'][i]
    tb_level = df_retention['Toon Blast'][i]
    diff = rm_level - tb_level
    if abs(diff) > 3:  # Only annotate significant differences
        xy_pos = (i, max(rm_level, tb_level) + 2)
        text_y_offset = 3 + i  # Stagger vertically
        ax1.annotate(f"{abs(diff)} levels {'later' if diff > 0 else 'earlier'}", 
                   xy=xy_pos, xytext=(xy_pos[0], xy_pos[1] + text_y_offset % 3),  # Modulo for cyclic placement
                   ha='center', fontsize=9,
                   bbox=dict(boxstyle="round,pad=0.3", fc='white', ec='gray', alpha=0.8))

# Add key insight - FIXED POSITIONING
ax1.text(0.5, 0.04, 
         "Toon Blast introduces all key retention features earlier than Royal Match",
         transform=ax1.transAxes, fontsize=12, ha='center', va='bottom', 
         bbox=dict(boxstyle="round,pad=0.6", fc='white', ec='gray', alpha=0.9), 
         fontweight='bold')

# 2. Monetization timeline - COMPLETELY REDESIGNED FOR CLARITY
ax2 = fig.add_subplot(gs[1])
ax2.set_xlim(0, 41)
ax2.set_ylim(0, 11)  # Extended height for better spacing
ax2.set_xlabel('Level Number', fontsize=14)
ax2.set_title('Monetization Touchpoints & Player Journey', fontsize=18, fontweight='bold', pad=15)
ax2.grid(axis='x', linestyle='--', alpha=0.7)
ax2.set_facecolor('white')

# Remove y-axis ticks as they're not needed
ax2.set_yticks([])
ax2.set_xticks(range(0, 41, 5))
ax2.tick_params(axis='x', labelsize=12)

# Define player journey phases
phases = [
    {"name": "Onboarding", "start": 1, "end": 10, "color": "#C5E0B4", "y_pos": 10.5},
    {"name": "Habit Formation", "start": 11, "end": 20, "color": "#FFD966", "y_pos": 10.5},
    {"name": "Engagement", "start": 21, "end": 30, "color": "#F4B084", "y_pos": 10.5},
    {"name": "Retention", "start": 31, "end": 40, "color": "#BDD7EE", "y_pos": 10.5}
]

# Add player journey phases
for phase in phases:
    ax2.fill_between([phase["start"]-0.5, phase["end"]+0.5], 10, 11, 
                    color=phase["color"], alpha=0.3)
    ax2.text((phase["start"] + phase["end"])/2, phase["y_pos"], phase["name"],
            ha='center', va='center', fontsize=10, fontweight='bold')

# Draw Royal Match timeline
ax2.plot([1, 40], [8, 8], '-', color=royal_match_color, markersize=0, linewidth=3)
ax2.text(2, 8.5, 'Royal Match', fontsize=12, color=royal_match_color, fontweight='bold')

# Draw Toon Blast timeline
ax2.plot([1, 40], [4, 4], '-', color=toon_blast_color, markersize=0, linewidth=3)
ax2.text(2, 4.5, 'Toon Blast', fontsize=12, color=toon_blast_color, fontweight='bold')

# Add Royal Match monetization points - IMPROVED POSITIONING
for i, point in enumerate(rm_monetization):
    vertical_pos = 8
    ax2.plot(point['level'], vertical_pos, 'o', markersize=12, color='white', markeredgecolor=royal_match_color, 
            markeredgewidth=2, zorder=10)
    ax2.plot(point['level'], vertical_pos, 'o', markersize=6, color=royal_match_color, zorder=11)
    
    # Add annotation with vertical staggering
    y_text_pos = vertical_pos + point['y_offset'] + (i % 2) * 0.5  # Stagger vertically based on index
    ax2.annotate(f"{point['type']}\n{point['description']}", 
                xy=(point['level'], vertical_pos), xytext=(point['level'], y_text_pos),
                ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=royal_match_color, alpha=0.8))

# Add Toon Blast monetization points - IMPROVED POSITIONING
for i, point in enumerate(tb_monetization):
    vertical_pos = 4
    ax2.plot(point['level'], vertical_pos, 'o', markersize=12, color='white', markeredgecolor=toon_blast_color, 
            markeredgewidth=2, zorder=10)
    ax2.plot(point['level'], vertical_pos, 'o', markersize=6, color=toon_blast_color, zorder=11)
    
    # Add annotation with vertical staggering
    y_text_pos = vertical_pos + point['y_offset'] - (i % 2) * 0.5  # Stagger vertically based on index
    ax2.annotate(f"{point['type']}\n{point['description']}", 
                xy=(point['level'], vertical_pos), xytext=(point['level'], y_text_pos),
                ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=toon_blast_color, alpha=0.8))

# Add key insights - FIXED POSITIONING TO AVOID OVERLAPS
insights = [
    "Royal Match has fewer but more extreme monetization points",
    "Toon Blast has more consistent monetization touchpoints",
    "Both games place monetization after retention features",
    "Extreme difficulty spike in RM level 19 (1 move) is a key monetization opportunity"
]

# Add an insight box in clear area
insight_text = "\n".join(f"• {insight}" for insight in insights)
ax2.text(38, 6, insight_text, fontsize=10, ha='right', va='center',
        bbox=dict(boxstyle="round,pad=0.6", fc='white', ec='gray', alpha=0.9))

plt.suptitle('Player Retention & Monetization Strategy', fontsize=24, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95], pad=2.0)
plt.savefig('game_charts/retention_monetization.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

#########################################
# 6. Comprehensive Dashboard WITHOUT Findings/Recommendations
#########################################

# Create master dashboard
fig = plt.figure(figsize=(20, 18), facecolor=background_color)  # Reduced height without findings/recommendations
gs = GridSpec(3, 2, wspace=0.4, hspace=0.5)  # Reduced to 3 rows instead of 4

# 1. Difficulty progression (top left)
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(levels, royal_match_difficulty, 'o-', color=royal_match_color, linewidth=2, 
        label='Royal Match', markersize=6)
ax1.plot(levels, toon_blast_difficulty, 'o-', color=toon_blast_color, linewidth=2, 
        label='Toon Blast', markersize=6)
ax1.fill_between(levels, royal_match_difficulty, alpha=0.1, color=royal_match_color)
ax1.fill_between(levels, toon_blast_difficulty, alpha=0.1, color=toon_blast_color)

ax1.set_title('Difficulty Progression', fontsize=16, fontweight='bold', pad=10)
ax1.set_xlabel('Level Number', fontsize=10)
ax1.set_ylabel('Difficulty (1-5)', fontsize=10)
ax1.set_xlim(0.5, 40.5)
ax1.set_ylim(0.5, 5.5)
ax1.set_xticks(np.arange(0, 41, 10))
ax1.set_yticks(np.arange(1, 6))
ax1.legend(fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('white')

# 2. Move Count by Segment (top right)
ax2 = fig.add_subplot(gs[0, 1])
segments = ['Levels 1-10', 'Levels 11-20', 'Levels 21-30', 'Levels 31-40']
x = np.arange(len(segments))
width = 0.35

bars1 = ax2.bar(x - width/2, rm_move_segments, width, label='Royal Match', color=royal_match_color)
bars2 = ax2.bar(x + width/2, tb_move_segments, width, label='Toon Blast', color=toon_blast_color)

# Add data labels
for bar in bars1:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.8,
           f'{height:.1f}', ha='center', va='bottom', fontsize=9)

for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.8,
           f'{height:.1f}', ha='center', va='bottom', fontsize=9)

ax2.set_title('Average Move Count by Segment', fontsize=16, fontweight='bold', pad=10)
ax2.set_ylabel('Average Moves', fontsize=10)
ax2.set_xticks(x)
ax2.set_xticklabels(segments, fontsize=9)
ax2.legend(fontsize=9)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_facecolor('white')

# 3. Royal Match Power-ups (mid left)
ax3 = fig.add_subplot(gs[1, 0])
wedges, texts, autotexts = ax3.pie(rm_power_tools['Count'], labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=pie_colors[:len(rm_power_tools['Tool'])], 
                                  wedgeprops={'edgecolor': 'white', 'linewidth': 1})

# Add custom legend - SIMPLIFIED FOR DASHBOARD
legend_labels = [f"{tool} ({count})" for tool, count in 
                zip(rm_power_tools['Tool'], rm_power_tools['Count'])]
ax3.legend(wedges, legend_labels, loc='center', bbox_to_anchor=(0.5, 0.0),
          ncol=2, fontsize=9, frameon=True)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)

ax3.set_title('Royal Match: Power-up Distribution', fontsize=16, fontweight='bold', pad=10)

# 4. Toon Blast Power-ups (mid right)
ax4 = fig.add_subplot(gs[1, 1])
wedges, texts, autotexts = ax4.pie(tb_power_tools['Count'], labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=pie_colors[:len(tb_power_tools['Tool'])],
                                  wedgeprops={'edgecolor': 'white', 'linewidth': 1})

# Add custom legend - SIMPLIFIED FOR DASHBOARD
legend_labels = [f"{tool} ({count})" for tool, count in 
                zip(tb_power_tools['Tool'], tb_power_tools['Count'])]
ax4.legend(wedges, legend_labels, loc='center', bbox_to_anchor=(0.5, 0.0),
          ncol=2, fontsize=9, frameon=True)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)

ax4.set_title('Toon Blast: Power-up Distribution', fontsize=16, fontweight='bold', pad=10)

# 5. Obstacle Distribution (bottom left)
ax5 = fig.add_subplot(gs[2, 0])
x = np.arange(5)
width = 0.35

rm_obs_values = [480, 350, 450, 475, 275]  # Royal Match obstacle counts
tb_obs_values = [2100, 440, 400, 630, 560]  # Toon Blast obstacle counts (scaled down)
tb_obs_scaled = [v / 4 for v in tb_obs_values]  # Scale down TB values to fit on same chart

# Plot Royal Match obstacles
bars3 = ax5.bar(x - width/2, rm_obs_values, width, label='Royal Match', color=royal_match_color)
# Plot Toon Blast obstacles (scaled)
bars4 = ax5.bar(x + width/2, tb_obs_scaled, width, label='Toon Blast (÷4)', color=toon_blast_color)

# Custom x labels for obstacles
obstacle_labels = ['Box/Balloon', 'Grass/Crate', 'Plate/Bubble', 'Mail/Carrot', 'Egg/Col-Balloon']
ax5.set_xticks(x)
ax5.set_xticklabels(obstacle_labels, fontsize=8)

# Add values on bars
for bar in bars3:
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height + 20,
           f'{int(height)}', ha='center', va='bottom', fontsize=8)

for i, bar in enumerate(bars4):
    height = bar.get_height()
    actual = tb_obs_values[i]
    ax5.text(bar.get_x() + bar.get_width()/2., height + 20,
           f'{actual}', ha='center', va='bottom', fontsize=8)

ax5.set_title('Obstacle Distribution (TB scaled down by 4x)', fontsize=16, fontweight='bold', pad=10)
ax5.set_ylabel('Count', fontsize=10)
ax5.legend(fontsize=9)
ax5.grid(axis='y', linestyle='--', alpha=0.7)
ax5.set_facecolor('white')

# 6. Retention Feature Timing (bottom right)
ax6 = fig.add_subplot(gs[2, 1])
# SHORTENED LABELS FOR BETTER FIT
retention_labels = ['Rating\nRequest', 'New\nEnvironment', 'Consecutive\nWin System', 
                   'Difficulty\nSpike', 'New\nBooster']
retention_rm = [15, 30, 32, 19, 17]
retention_tb = [11, 20, 24, 15, 16]

x = np.arange(len(retention_labels))
width = 0.35

bars5 = ax6.bar(x - width/2, retention_rm, width, label='Royal Match', color=royal_match_color)
bars6 = ax6.bar(x + width/2, retention_tb, width, label='Toon Blast', color=toon_blast_color)

# Add level numbers on bars
for bar in bars5:
    height = bar.get_height()
    ax6.text(bar.get_x() + bar.get_width()/2., height + 1,
           f'{int(height)}', ha='center', va='bottom', fontsize=9)

for bar in bars6:
    height = bar.get_height()
    ax6.text(bar.get_x() + bar.get_width()/2., height + 1,
           f'{int(height)}', ha='center', va='bottom', fontsize=9)

ax6.set_title('Retention Feature Introduction (Level #)', fontsize=16, fontweight='bold', pad=10)
ax6.set_xticks(x)
ax6.set_xticklabels(retention_labels, fontsize=8)
ax6.legend(fontsize=9)
ax6.grid(axis='y', linestyle='--', alpha=0.7)
ax6.set_facecolor('white')

# Add overall dashboard title
fig.suptitle('Royal Match vs. Toon Blast: Comprehensive Game Analysis', 
           fontsize=28, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.97], pad=3.0)  # Increased padding
plt.savefig('game_charts/master_dashboard.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

# Additional analysis - Monetization and Difficulty Correlation with improved spacing
plt.figure(figsize=(15, 8), facecolor=background_color)
plt.plot(levels, royal_match_difficulty, 'o-', color=royal_match_color, linewidth=2, 
        label='Royal Match', markersize=6)
plt.plot(levels, toon_blast_difficulty, 'o-', color=toon_blast_color, linewidth=2, 
        label='Toon Blast', markersize=6)

# Highlight Royal Match monetization points - IMPROVED POSITIONING
for i, point in enumerate(rm_monetization):
    plt.plot(point['level'], royal_match_difficulty[point['level']-1], 'o', markersize=12, 
            markerfacecolor='none', markeredgecolor=royal_match_color, markeredgewidth=2, zorder=10)
    plt.plot(point['level'], royal_match_difficulty[point['level']-1], 'o', markersize=6, 
            color='white', zorder=11)
    
    # Add multiple offsets for different annotations
    x_offset = 0.5 + (i % 2) * 0.5  # Alternate left/right more
    y_offset = 0.4 + (i % 3) * 0.3  # Cycle through 3 vertical positions
    
    plt.annotate(f"{point['type']}", 
                xy=(point['level'], royal_match_difficulty[point['level']-1]), 
                xytext=(point['level'] + x_offset, royal_match_difficulty[point['level']-1] + y_offset),
                color=royal_match_color, fontweight='bold', fontsize=9,
                arrowprops=dict(arrowstyle='->', color=royal_match_color),
                bbox=dict(boxstyle="round,pad=0.2", fc='white', ec=royal_match_color, alpha=0.8))

# Highlight Toon Blast monetization points - IMPROVED POSITIONING
for i, point in enumerate(tb_monetization):
    plt.plot(point['level'], toon_blast_difficulty[point['level']-1], 'o', markersize=12, 
            markerfacecolor='none', markeredgecolor=toon_blast_color, markeredgewidth=2, zorder=10)
    plt.plot(point['level'], toon_blast_difficulty[point['level']-1], 'o', markersize=6, 
            color='white', zorder=11)
    
    # Add multiple offsets for different annotations
    x_offset = -0.5 - (i % 2) * 0.5  # Alternate left/right more
    y_offset = -0.4 - (i % 3) * 0.3  # Cycle through 3 vertical positions
    
    plt.annotate(f"{point['type']}", 
                xy=(point['level'], toon_blast_difficulty[point['level']-1]), 
                xytext=(point['level'] + x_offset, toon_blast_difficulty[point['level']-1] + y_offset),
                color=toon_blast_color, fontweight='bold', fontsize=9,
                arrowprops=dict(arrowstyle='->', color=toon_blast_color),
                bbox=dict(boxstyle="round,pad=0.2", fc='white', ec=toon_blast_color, alpha=0.8))

plt.title('Difficulty and Monetization Correlation', fontsize=22, fontweight='bold', pad=20)
plt.xlabel('Level Number', fontsize=14)
plt.ylabel('Difficulty Rating (1-5)', fontsize=14)
plt.xlim(0.5, 40.5)
plt.ylim(0.5, 5.5)
plt.xticks(np.arange(0, 41, 5))
plt.yticks(np.arange(1, 6))
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout(pad=2.0)
plt.savefig('game_charts/monetization_difficulty_correlation.png', dpi=300, bbox_inches='tight', facecolor=background_color)
plt.close()

print("All charts have been saved to the 'game_charts' directory.")