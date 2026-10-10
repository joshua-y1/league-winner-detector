with source as (
    select * from {{ source('raw', 'player_stats') }}
)

select
    player_id,
    player_display_name as player_name,
    position,
    team, 
    season,
    week,
    coalesce(targets, 0) as targets,
    coalesce(carries, 0) as carries,
    coalesce(receptions, 0) as receptions,
    target_share,
    air_yards_share,
    wopr,
    rushing_yards,
    receiving_yards,
    rushing_tds,
    receiving_tds,
    fantasy_points_ppr
from source
