import nflreadpy as nfl

stats = nfl.load_player_stats([2025]).to_pandas()
print(stats.shape)
print(stats.columns.tolist())
print(stats.head())