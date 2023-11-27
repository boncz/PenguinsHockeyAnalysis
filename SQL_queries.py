playoff_2016_data_query = ('''
SELECT game_plays_trimmed.*,
       game_plays_players.*, 
       player_info.firstName, 
       player_info.lastName 
 
FROM game
JOIN game_plays_trimmed ON game.game_id = game_plays_trimmed.game_id
JOIN game_plays_players ON game_plays_trimmed.play_id = game_plays_players.play_id
JOIN player_info ON game_plays_players.player_id = player_info.player_id

WHERE game.type = 'P'
    AND game.season = 20152016 

    AND (
        game.home_team_id = 5
        OR
        game.away_team_id = 5
        );
''')

playoff_2017_data_query = ('''
SELECT game_plays_trimmed.*,
       game_plays_players.*, 
       player_info.firstName, 
       player_info.lastName 

FROM game
JOIN game_plays_trimmed ON game.game_id = game_plays_trimmed.game_id
JOIN game_plays_players ON game_plays_trimmed.play_id = game_plays_players.play_id
JOIN player_info ON game_plays_players.player_id = player_info.player_id

WHERE game.type = 'P'
    AND game.season = 20162017 

    AND (
        game.home_team_id = 5
        OR
        game.away_team_id = 5
        );
''')



skater_stats_2016_query = ('''
SELECT skater_stats.*, team_info.abbreviation
FROM (
    SELECT game_skater_stats.*,
       player_info.firstName,
       player_info.lastName,
       player_info.primaryPosition
FROM game_skater_stats
JOIN player_info ON game_skater_stats.player_id = player_info.player_id) skater_stats


LEFT JOIN game ON skater_stats.game_id = game.game_id
JOIN team_info ON skater_stats.team_id = team_info.team_id
WHERE game.season = 20152016
      AND game.type = 'P'
      AND (game.away_team_id = 5
      OR   game.home_team_id = 5)
      ;
''')

skater_stats_2017_query = ('''
SELECT skater_stats.*, team_info.abbreviation
FROM (
    SELECT game_skater_stats.*,
       player_info.firstName,
       player_info.lastName,
       player_info.primaryPosition
FROM game_skater_stats
JOIN player_info ON game_skater_stats.player_id = player_info.player_id) skater_stats


LEFT JOIN game ON skater_stats.game_id = game.game_id
JOIN team_info ON skater_stats.team_id = team_info.team_id
WHERE game.season = 20162017
      AND game.type = 'P'
      AND (game.away_team_id = 5
      OR   game.home_team_id = 5)
      ;
''')


goals_query = ('''
SELECT  game_goals.*, 
        game_plays_trimmed.event,
        game_plays_trimmed.secondaryType,
        game_plays_trimmed.x,
        game_plays_trimmed.y,
        game_plays_players.playerType,
        player_info.firstName,
        player_info.lastName
FROM game_goals

JOIN game_plays_trimmed ON game_goals.play_id = game_plays_trimmed.play_id
JOIN game_plays_players ON game_plays_trimmed.player_id = game_plays_players.player_id
JOIN player_info ON game_plays_players.player_id = player_info.player_id
;
''')

get_abb_query = ('''
SELECT  team_info.team_id,
        team_info.abbreviation
FROM team_info;
''')