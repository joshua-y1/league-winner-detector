select
    player_id,
    week,
    count(*) as row_count
from {{ ref('stg_player_stats') }}
group by player_id, week
having count(*) > 1