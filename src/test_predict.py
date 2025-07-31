# src/test_predict.py

from predict import load_player_data, add_goals_per_game, scoring_probability

# Load your cleaned player data
df = load_player_data("data/gignac_cleaned.csv")

# For now, manually add goals + games (you'll automate this later)
df["goals"] = 14      # ← replace this with real total goals for Gignac
df["games"] = 28      # ← replace this with real total games played

# Add new column: goals per game
df = add_goals_per_game(df, "goals", "games")

# Pick first player row
player = df.iloc[0]
gpg = player["goals_per_game"]

# Predict: probability of 2+ goals using Poisson
chance = scoring_probability(goals_per_game=gpg, goal_count=2)

print(f"{player['name']} has a {chance:.2%} chance of scoring 2+ goals.")
