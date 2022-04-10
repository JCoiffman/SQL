-- Data Manipulation Queries
--$data represents user input

-- LEAGUE HISTORIES

-- League Histories Page select query 
SELECT * FROM league_histories;

-- League Histories Page insert query
INSERT INTO league_histories (league_name, completed_seasons_num)
VALUES ($leagueName, $completedSeasonsNum);

-- League Histories Page update query
UPDATE league_histories
SET league_name = $leagueName, completed_seasons_num = $completedSeasonsNum
WHERE league_id = $id;

-- League Histories Page delete query
DELETE FROM league_histories WHERE league_id = $id;

-- SEASONS

-- Seasons Page select query
SELECT * FROM seasons;

-- Seasons Page insert query
INSERT INTO seasons (league_id, season_name, date_season_started, 
date_season_ended, league_champion, western_champion, 
eastern_champion, most_valuable_player, sixth_man_of_the_year)
VALUES ($leagueID, $seasonName, $dateSeasonStarted, 
$dateSeasonEnded, $leagueChampion, $westernChampion, 
$easternChampion, $mostValuablePlayer, $defensivePlayerOfTheYear, 
$mostImprovedPlayerOfTheYear, $sixthManOfTheYear);

-- Seasons Page update query
UPDATE seasons
SET league_id = $leagueID, season_name = $seasonName, date_season_started = $dateSeasonStarted, 
date_season_ended = $dateSeasonEnded, league_champion = $leagueChampion, western_champion = $westernChampion, 
eastern_champion = $easternChampion, most_valuable_player = $mostValuablePlayer, defensive_player_of_the_year = $defensivePlayerOfTheYear, 
most_improved_player_of_the_year = $mostImprovedPlayerOfTheYear, sixth_man_of_the_year = $sixthManOfTheYear
WHERE season_id = $id;

-- Seasons Page delete query
DELETE FROM seasons WHERE season_id = $id;

-- TEAMS

-- Teams Page select query
SELECT * FROM teams;

-- Teams Page insert query
INSERT INTO teams (season_id, team_name, team_place_city, 
team_place_state, points_per_game, assists_per_game, 
steals_per_game, blocks_per_game, rebounds_per_game, 
fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game,
fg_percentage, three_pt_fg_percentage, ft_percentage,
point_differential, reg_season_wins, reg_season_losses, 
reg_season_win_percentage)
VALUES ($seasonID, $teamName, $teamPlaceCity, 
$teamPlaceState, $pointsPerGame, $assistsPerGame, 
$stealsPerGame, $blocksPerGame, $reboundsPerGame, 
$foulsPerGame, $fgAttemptedPerGame, $threePtfgAttemptedPerGame, 
$fgPercentage, $threePtfgPercentage, $ftPercentage, 
$pointDifferential, $regSeasonWins, $regSeasonLosses, 
$regSeasonWinPercentage);

-- Teams Page update query
UPDATE teams
SET season_id = $seasonID, team_name = $teamName, team_place_city = $teamPlaceCity, 
team_place_state = $teamPlaceState, points_per_game = $pointsPerGame, assists_per_game = $assistsPerGame, 
steals_per_game = $stealsPerGame, blocks_per_game = $blocksPerGame, rebounds_per_game = $reboundsPerGame, 
fouls_per_game = $foulsPerGame, fg_attempted_per_game = $fgAttemptedPerGame, three_pt_fg_attempted_per_game = $threePtfgAttemptedPerGame, 
fg_percentage = $fgPercentage, three_pt_fg_percentage = $threePtfgPercentage, ft_percentage = $ftPercentage, 
point_differential = $pointDifferential, reg_season_wins = $regSeasonWins, reg_season_losses = $regSeasonLosses, 
reg_season_win_percentage = $regSeasonWinPercentage
WHERE team_id = $id;

-- Teams Page delete query
DELETE FROM teams WHERE team_id = $id;

-- PLAYERS

-- Players Page select query
SELECT * FROM players;

-- Players Page insert query
INSERT INTO players (player_name, player_jersey_number, player_height_feet, 
player_height_inch, points_per_game, assists_per_game, 
steals_per_game, blocks_per_game, rebounds_per_game, 
fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, 
ft_attempted_per_game, ft_percentage, plus_minus)
VALUES ($playerName, $playerJerseyNumber, $player_height_feet, 
$playerHeightInch, $pointsPerGame, $assistsPerGame, 
$stealsPerGame, $blocksPerGame, $reboundsPerGame, 
$foulsPerGame, $fgAttemptedPerGame, $threePtfgAttemptedPerGame, 
$ftAttemptedPerGame, $ftPercentage, $plusMinus);

-- Players Page update query
UPDATE players
SET player_name = $playerName, player_jersey_number = $playerJerseyNumber, player_height_feet = $player_height_feet, 
player_height_inch = $playerHeightInch, points_per_game = $pointsPerGame, assists_per_game = $assistsPerGame, 
steals_per_game = $stealsPerGame, blocks_per_game = $blocksPerGame, rebounds_per_game = $reboundsPerGame, 
fouls_per_game = $foulsPerGame, fg_attempted_per_game = $fgAttemptedPerGame, three_pt_fg_attempted_per_game = $threePtfgAttemptedPerGame, 
ft_attempted_per_game = $ftAttemptedPerGame, ft_percentage = $ftPercentage, plus_minus = $plusMinus
WHERE player_id = $id;

-- Players Page delete query
DELETE FROM players WHERE player_id = $id;

-- PLAYER TEAM RELATIONS

-- Player Team Relations Page select query
SELECT * FROM player_team_relations;

-- Player Team Relations Page insert query
INSERT INTO player_team_relations (player_id, team_id)
VALUES ($playerID, $teamID);

-- Player Team Relations Page update query
UPDATE player_team_relations
SET player_id = $playerID, team_id = $teamID
WHERE player_team_id = $id;

-- Player Team Relations Page delete query
DELETE FROM player_team_relations WHERE player_team_id = $id;

-- COACHES

-- Coaches Page select query
SELECT * FROM coaches;

-- Coaches Page insert query
INSERT INTO coaches (coach_name, coach_wins, coach_losses, coach_win_percentage)
VALUES ($coachName, $coachWins, $coachLosses, $coachWinPercentage);

-- Coaches Page update query
UPDATE coaches
SET coach_name = $coachName, coach_wins = $coachWins, coach_losses = $coachLosses, 
coach_win_percentage = $coachWinPercentage
WHERE coach_id = $id;

-- Coaches Page delete query
DELETE FROM coaches WHERE coach_id = $id;

-- COACH TEAM RELATIONS

-- Coach Team Relations Page select query
SELECT * FROM coach_team_relations;

-- Coach Team Relations Page insert query
INSERT INTO coach_team_relations (coach_id, team_id)
VALUES ($coachID, $teamID);

-- Coach Team Relations Page update query
UPDATE coach_team_relations
SET coach_id = $coachID, team_id = $teamID
WHERE coach_team_id = $id;

-- Coach Team Relations Page delete query
DELETE FROM coach_team_relations WHERE coach_team_id = $id;
