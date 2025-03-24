# Obstacle and Power-Up Distribution Analysis

Based on the JSON data analysis, here's a breakdown of how obstacles and power-ups are distributed across both games:

## Royal Match

### Move Count Analysis
- **Average moves per level:** 25.5
- **Average unused moves:** 8.0
- **Move count by segment:**
  - Levels 1-10: 27.1 (Onboarding phase)
  - Levels 11-20: 25.0 (Introducing complexity)
  - Levels 21-30: 24.8 (Challenging mid-game)
  - Levels 31-40: 23.5 (Endgame challenge)

### Obstacle Distribution
- **Box:** 480+ total instances (First appears in level 4)
- **Grass:** 350+ total instances (First appears in level 5)
- **Plate:** 450+ total instances (First appears in level 11)
- **Mail:** 475+ total instances (First appears in level 21)
- **Egg:** 275+ total instances (First appears in level 31)

### Power Tool Usage
- **TNT:** 83 total uses
- **Propeller:** 93 total uses
- **Rocket:** 119 total uses
- **Light Ball:** 40 total uses

### Key Insights:
1. Royal Match shows a clear pattern of gradually decreasing move counts as players progress
2. New obstacles are introduced systematically at approximately 10-level intervals
3. Rockets are the most frequently used power tool, while Light Balls are the rarest

## Toon Blast

### Move Count Analysis
- **Average moves per level:** 30.7
- **Average unused moves:** 9.5
- **Move count by segment:**
  - Levels 1-10: 41.2 (Generous onboarding)
  - Levels 11-20: 24.5 (Significant reduction in moves)
  - Levels 21-30: 28.1 (Slight easing after difficulty spike)
  - Levels 31-40: 29.3 (Consistent endgame challenge)

### Obstacle Distribution
- **Balloon:** 2100+ total instances (First appears in level 1)
- **Crate:** 440+ total instances (First appears in level 4)
- **Bubble:** 400+ total instances (First appears in level 11)
- **Carrot:** 630+ total instances (First appears in level 21)
- **Colored-Balloon:** 560+ total instances (First appears in level 31)

### Power Tool Usage
- **Bomb:** 70+ total uses
- **Rocket:** 110+ total uses
- **Disco Ball:** 135+ total uses

### Key Insights:
1. Toon Blast begins with extremely generous move counts that drastically reduce after level 10
2. Similar to Royal Match, new obstacles are introduced at approximately 10-level intervals
3. Disco Balls are the most frequently used power tool, while Bombs are the least common
4. Balloon obstacles have by far the highest count, appearing in massive quantities in certain levels (e.g., level 20 with 500 balloons)

## Comparative Analysis

### Move Count Patterns
- Toon Blast offers 22% more moves on average than Royal Match (30.7 vs 25.5)
- Toon Blast shows a more dramatic reduction in moves after onboarding (41.2 → 24.5)
- Royal Match has a more gradual reduction in moves throughout all segments

### Obstacle Patterns
- Both games introduce new obstacles every ~10 levels
- Toon Blast has significantly higher obstacle counts overall
- Royal Match has more even distribution across obstacle types
- Both games use their first obstacle consistently throughout (Box for Royal Match, Balloon for Toon Blast)

### Power-Up Patterns
- Both games favor certain power-ups (Rockets in Royal Match, Disco Balls in Toon Blast)
- Royal Match has more power-up variety (4 types vs 3 types)
- Toon Blast shows higher overall power-up usage
