SELECT
    player_id,
    week,
    count(*) AS row_count
FROM {{ ref('stg_player_stats') }}
GROUP BY player_id, week
HAVING count(*) > 1