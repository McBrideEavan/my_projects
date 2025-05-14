# 📊 **Roster Consistency and Team Performance Analysis**

**Author:** Eavan McBride  
**Hypothesis:** Higher roster consistency from game to game correlates with higher win percentage.  
**Scope:** Minnesota Wild NHL Season 2025  
**Context:**  
My dad is a big Wild Hockey fan, and during one of our conversations, he mentioned how NHL teams can make trades and roster adjustments up until mid-season. He also noted that teams in the playoffs often have a much different lineup than the one they started the season with. This sparked a curiosity:  
> *Would teams that maintain a more consistent lineup throughout the season perform better on average?*  

This project aims to explore that hypothesis by measuring **roster consistency** game-over-game for the Minnesota Wild during the 2025 NHL season and correlating it with their **win percentage**.  

---

## 📝 **Project Structure**
|-- data/ # Raw and processed data files
|-- notebooks/ # Jupyter Notebooks for step-by-step analysis
|-- src/ # Core Python scripts
| |-- data_collection.py # Script to collect game and roster data
| |-- analysis.py # Script to calculate consistency metrics
| |-- visualization.py # Script to generate plots and analytics
|-- README.md # Project documentation (you are reading this!)
|-- requirements.txt # List of dependencies
|-- main.py # Main execution script

---

## ⚙️ **Setup Instructions**
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/McBrideEavan/nhl-roster-consistency.git
   cd nhl-roster-consistency
2. **Install Dependencies:**
    pip install -r requirements.txt
3. **Run the analysis:**
    python main.py
4.  **Launch Jupyter for step-by-step walkthrough:**
    jupyter notebook notebooks/analysis.ipynb

---

## 📌 **Methodology**
### 1. **Data Collection:**

    - Game schedule and rosters are fetched using the NHL Stats API.

    - Roster information is extracted for each game played during the season.

### 2. **Roster Consistency Calculation:**

     - Game-over-game consistency is measured using the Jaccard Similarity Index, which quantifies the overlap of players between consecutive games.

### 3. **Team Performance Metrics:**

    - Win/Loss records and goal differentials are recorded for each game.

### 4. **Correlation Analysis:**

    - Statistical analysis is performed to identify any correlation between roster consistency and team performance.

---

## 📊 **Results and Visualization**
Results are plotted to visually interpret any correlation between consistency and win percentage.

 - Line plots to show changes in roster similarity over the season.

 - Scatter plots to visualize correlation with win percentage.

---

## 🔍 **Future Improvements**
 - Expand analysis to all NHL teams for broader insight.

 - Include playoff roster stability versus regular season.

 - Account for player-specific impact (e.g., injuries, key trades).

---
