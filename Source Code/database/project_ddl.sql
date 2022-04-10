-- Data Definition Queries

-- Drop table to reset database
DROP TABLE IF EXISTS `league_histories`;
DROP TABLE IF EXISTS `seasons`;
DROP TABLE IF EXISTS `teams`;
DROP TABLE IF EXISTS `players`;
DROP TABLE IF EXISTS `player_team_relations`;
DROP TABLE IF EXISTS `coaches`;
DROP TABLE IF EXISTS `coach_team_relations`;

-- Data Definition Queries

-- Create League Histories Table
CREATE TABLE league_histories (
  league_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  league_name varchar(255) NOT NULL,
  completed_seasons_num int(11) NOT NULL
);

-- Create Seasons Table
CREATE TABLE seasons (
  season_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  league_id int(11) NOT NULL,
  season_name varchar(255) NOT NULL,
  date_season_started date NOT NULL,
  date_season_ended date NOT NULL,
  league_champion varchar(255) NOT NULL,
  western_champion varchar(255) NOT NULL,
  eastern_champion varchar(255) NOT NULL,
  most_valuable_player varchar(255) NOT NULL,
  defensive_player_of_the_year varchar(255) NOT NULL,
  most_improved_player_of_the_year varchar(255) NOT NULL,
  sixth_man_of_the_year varchar(255) NOT NULL,
  FOREIGN KEY (league_id) REFERENCES league_histories(league_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Create Teams table
CREATE TABLE teams (
  team_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  season_id int(11) NOT NULL,
  team_name varchar(255) NOT NULL,
  team_place_city varchar(255) NOT NULL,
  team_place_state varchar(255) NOT NULL,
  points_per_game decimal(5, 1) NOT NULL,
  assists_per_game decimal(5, 1) NOT NULL,
  steals_per_game decimal(5, 1) NOT NULL,
  blocks_per_game decimal(5, 1) NOT NULL,
  rebounds_per_game decimal(5, 1) NOT NULL,
  fouls_per_game decimal(5, 1) NOT NULL,
  fg_attempted_per_game decimal(5, 1) NOT NULL,
  three_pt_fg_attempted_per_game decimal(5, 1) NOT NULL,
  ft_attempted_per_game decimal(5, 1) NOT NULL,
  fg_percentage decimal(5, 3) NOT NULL,
  three_pt_fg_percentage decimal(5, 3) NOT NULL,
  ft_percentage decimal(5, 3) NOT NULL,
  point_differential decimal(5, 1) NOT NULL,
  reg_season_wins_num int(11) NOT NULL,
  reg_season_losses_num int(11) NOT NULL,
  reg_season_win_percentage decimal(5, 3) NOT NULL,
  FOREIGN KEY (season_id) REFERENCES seasons(season_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Create Players table
CREATE TABLE players (
  player_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  team_id int(11) NOT NULL,
  player_name varchar(255) NOT NULL,
  player_jersey_number int(11) NOT NULL, 
  player_height_feet int(11) NOT NULL,
  player_height_inch int(11) NOT NULL,
  points_per_game decimal(5, 1),
  assists_per_game decimal(5, 1),
  steals_per_game decimal(5, 1),
  blocks_per_game decimal(5, 1),
  rebounds_per_game decimal(5, 1), 
  fouls_per_game decimal(5, 1),
  fg_attempted_per_game decimal(5, 1),
  three_pt_fg_attempted_per_game decimal(5, 1),
  ft_attempted_per_game decimal(5, 1),
  fg_percentage decimal(5, 3),
  three_pt_fg_percentage decimal(5, 3),
  ft_percentage decimal(5, 3),
  plus_minus decimal(5, 1)
);

-- Create Player Team Relations table
CREATE TABLE player_team_relations (
  player_team_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  player_id int(11) NOT NULL,
  team_id int(11) NOT NULL,
  FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Coaches Table
CREATE TABLE coaches (
  coach_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  team_id int(11) NOT NULL,
  coach_name varchar(255) NOT NULL,
  coach_wins int(11) NOT NULL,
  coach_losses int(11) NOT NULL,
  coach_win_percentage dec(5, 3)
);

-- Create Coach Team Relations table
CREATE TABLE coach_team_relations (
  coach_team_id int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  coach_id int(11) NOT NULL,
  team_id int(11) NOT NULL,
  FOREIGN KEY (coach_id) REFERENCES coaches(coach_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert values into League Histories table
INSERT INTO league_histories (league_name, completed_seasons_num)
VALUES ("NBA", "74"),
("WNBA", "24"),
("Euroleague", "63");

-- Insert values into Seasons table
INSERT INTO seasons (league_id, season_name, date_season_started, 
date_season_ended, league_champion, western_champion, 
eastern_champion, most_valuable_player, defensive_player_of_the_year, 
most_improved_player_of_the_year, sixth_man_of_the_year)
VALUES ("1", "2000-2001", "2000-10-31", 
"2001-04-18", "Los Angeles Lakers", "Los Angeles Lakers", 
"Philadelphia 76ers", "Allen Iverson", "Dikembe Mutombo", 
"Tracy McGrady", "Aaron McKie"),
("1", "2005-2006", "2005-11-01", 
"2006-04-19", "Miami Heat", "Dallas Mavericks", 
"Miami Heat", "Steve Nash", "Ben Wallace", 
"Boris Diaw", "Mike Miller"),
("1", "2010-2011", "2010-10-26", 
"2011-04-13", "Dallas Mavericks", "Dallas Mavericks", 
"Miami Heat", "Derrick Rose", "Dwight Howard", 
"Kevin Love", "Lamar Odom");

-- Insert values into Teams table
INSERT INTO teams (season_id, team_name, team_place_city, 
team_place_state, points_per_game, assists_per_game, 
steals_per_game, blocks_per_game, rebounds_per_game, 
fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, 
ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, 
ft_percentage, point_differential, reg_season_wins_num, 
reg_season_losses_num, reg_season_win_percentage)
VALUES ("1", "Los Angeles Lakers", "Los Angeles", 
"California", "100.6", "23.0", 
"6.9", "6.0", "44.7", 
"22.8", "81.5", "15.5", 
"28.5", "0.465", "0.344", 
"0.683", "3.2", "56", 
"26", "0.683"),
("2", "Miami Heat", "Miami", 
"Florida", "99.9", "20.6", 
"6.4", "5.4", "43.1", 
"22.8", "77.5", "17.6", 
"19.7", "0.478", "0.345", 
"0.700", "3.9", "52", 
"30", "0.634"),
("3", "Dallas Mavericks", "Dallas", 
"Texas", "100.2", "23.8", 
"6.8", "4.3", "41.5", 
"19.2", "78.8", "21.6", 
"22.6", "0.475", "0.365", 
"0.777", "4.2", "57", 
"25", "0.695");

-- Insert values into Players table
INSERT INTO players (team_id, player_name, player_jersey_number, player_height_feet, 
player_height_inch, points_per_game, assists_per_game, 
steals_per_game, blocks_per_game, rebounds_per_game, 
fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, 
ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, 
ft_percentage, plus_minus)
VALUES ("1", "Shaquille O''Neal", "34", "7", 
"1", "28.7", "3.7", 
"0.6", "2.8", "12.7", 
"3.5", "19.2", "0.0", 
"13.1", "0.572", "0.000", 
"0.513", "8.0"),
("2", "Dwyane Wade", "3", "6", 
"4", "27.2", "6.7", 
"1.9", "0.8", "5.7", 
"2.9", "18.8", "1.0", 
"10.7", "0.495", "0.171", 
"0.783", "8.3"),
("3", "Dirk Nowitzki", "41", "7", 
"0", "23.0", "2.6", 
"0.5", "0.6", "7.0", 
"2.4", "16.2", "2.3", 
"6.1", "0.517", "0.393", 
"0.892", "10.6");

-- Insert values into Player Team Relations table
INSERT INTO player_team_relations (player_id, team_id)
VALUES ("1", "1"), ("2", "2"), ("3", "3");

-- Insert values into Coaches table
INSERT INTO coaches (team_id, coach_name, coach_wins, coach_losses, 
coach_win_percentage)
VALUES ("1", "Phil Jackson", "56", "26", "0.683"),
("2", "Pat Riley", "41", "20", "0.671"),
("3", "Rick Carlisle", "57", "25", "0.695");

-- Insert values into Coach Team Relations table
INSERT INTO coach_team_relations (coach_id, team_id)
VALUES ("1", "1"), ("2", "2"), ("3", "3");
