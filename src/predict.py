# src/predict.py

import pandas as pd
from scipy.stats import poisson

# 1. Load your cleaned player data
def load_player_data(filepath):
    df = pd.read_csv(filepath)
    return df

# 2. Add a new column: goals per game (GPG)
def add_goals_per_game(df, total_goals_col, total_games_col):
    df["goals_per_game"] = df[total_goals_col] / df[total_games_col]
    return df

# 3. Poisson-based probability of scoring at least X goals
def scoring_probability(goals_per_game, goal_count=1):
    """
    Calculates the probability of scoring at least `goal_count` goals
    using the Poisson distribution.
    """
    from scipy.stats import poisson
    return 1 - poisson.cdf(goal_count - 1, goals_per_game)
