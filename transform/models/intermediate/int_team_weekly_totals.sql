SELECT
    team,
    season,
    week,
    sum(carries) AS team_carries,
    sum(targets) AS team_targets
FROM {{ ref('stg_player_stats') }}
GROUP BY team, season, week