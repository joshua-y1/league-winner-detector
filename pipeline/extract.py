import nflreadpy as nfl
import pandas as pd
from pathlib import Path

SEASON = 2025
POSITIONS = ["RB", "WR", "TE"]
COLUMNS = [
    "player_id", "player_display_name", "position", "team",
    "season", "week", "season_type",
    "targets", "carries", "receptions", "target_share", "air_yards_share", "wopr",
    "rushing_yards", "receiving_yards", "rushing_tds", "receiving_tds", "fantasy_points_ppr",
]

def section(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")


def extract(season):
    # 1. pull the season and convert to pandas
    df = nfl.load_player_stats([season]).to_pandas()
    # 2. keep only COLUMNS
    df = df[COLUMNS]
    # 3. filter to regular season and POSITIONS
    is_position = df["position"].isin(POSITIONS)
    is_regular = df["season_type"] == "REG"
    df = df[is_position & is_regular]
    # 4. return to dataframe
    return df


if __name__ == "__main__":
    df = extract(SEASON)
    # print the shape so you can sanity-check it
    section("Shape")
    print(f"{df.shape[0]:,} rows x {df.shape[1]} columns")
    
    # save to data/raw/player_stats_{SEASON}.parquet 
    Path("data/raw").mkdir(parents=True, exist_ok=True)         
    df.to_parquet(f"data/raw/player_stats_{SEASON}.parquet", index=False)  
    
    # print DB Head
    section("Saved file preview")
    print(pd.read_parquet(f"data/raw/player_stats_{SEASON}.parquet").head())
    

