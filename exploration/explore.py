import nflreadpy as nfl

stats = nfl.load_player_stats([2025]).to_pandas()

def section(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")

section("Shape")
print(f"{stats.shape[0]:,} rows x {stats.shape[1]} columns")

section("First 5 rows")
print(stats[["player_display_name", "position", "team", "week", "season_type"]].head())

section("Grain check")
print(f"Unique players:         {stats['player_id'].nunique():,}")
print(f"Weeks:                  {[int(w) for w in sorted(stats['week'].unique())]}")
print(f"Duplicate player-weeks: {stats.duplicated(subset=['player_id', 'week']).sum()}")

section("Usage-related columns")
keywords = ["target", "carr", "recep", "share", "wopr", "snap", "air"]
for col in [
      c for c in stats.columns 
      if any (k in c for k in keywords) and c != "pt_fair_caught"
    ]:
    print(f"  - {col}")