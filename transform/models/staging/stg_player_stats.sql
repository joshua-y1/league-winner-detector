WITH source AS (
    SELECT * FROM {{ source('raw', 'player_stats') }}
)

SELECT
    player_id,
    player_display_name AS player_name,
    position,
    team, 
    season,
    week,
    coalesce(targets, 0) AS targets,
    coalesce(carries, 0) AS carries,
    coalesce(receptions, 0) AS receptions,
    target_share,
    air_yards_share,
    wopr,
    rushing_yards,
    receiving_yards,
    rushing_tds,
    receiving_tds,
    fantasy_points_ppr
FROM source
