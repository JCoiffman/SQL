from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
webapp = Flask(__name__)

# ***************************************************************************************/
# *    Title: Using Python Flask on the Engineering Servers
# *    Author: Hedaoo, Samarendra M
# *    Date: 2020
# *    Code version: 1.4.3
# *    Availability: https://github.com/knightsamar/CS340_starter_flask_app
# *
# ***************************************************************************************/

# Home page
@webapp.route('/index')
def index():
    db_connection = connect_to_database()
    return render_template('index.html')

# League histories READ + CREATE functions
@webapp.route('/league_histories', methods=['POST','GET'])
def league_histories():
    db_connection = connect_to_database()

    # READ function
    if request.method == 'GET':    
        print("Fetching and rendering league_histories web page")
        query = 'SELECT league_id, league_name, completed_seasons_num from league_histories'
        result = execute_query(db_connection, query).fetchall()
        return render_template("league_histories.html", rows=result)
    
    # CREATE function
    elif request.method == 'POST':
        print("Add new league histories!")
        league_name = request.form['league_name']
        completed_seasons_num = request.form['completed_seasons_num']

        query = 'INSERT INTO league_histories (league_name, completed_seasons_num) VALUES (%s,%s)'
        data = (league_name, completed_seasons_num)
        execute_query(db_connection, query, data)

        query = 'SELECT league_id, league_name, completed_seasons_num from league_histories'
        result = execute_query(db_connection, query).fetchall()
        return render_template("league_histories.html", rows=result)

# League histories DELETE function
@webapp.route('/delete_league_histories/<int:league_id>')
def delete_league_histories(league_id):
    '''deletes a league history with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM league_histories WHERE league_id = %s"
    data = (league_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/league_histories')

# League histories UPDATE function
@webapp.route('/update_league_histories/<int:league_id>', methods=['POST','GET'])
def update_league_histories(league_id):
    print('In the function')
    db_connection = connect_to_database()
    
    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')
        league_histories_query = 'SELECT league_id, league_name, completed_seasons_num from league_histories WHERE league_id = %s'  % (league_id)
        league_histories_result = execute_query(db_connection, league_histories_query).fetchone()

        if league_histories_result == None:
            return "No such league history found!"

        print('Returning')
        return render_template('update_league_histories.html', league_histories = league_histories_result)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        league_id = request.form['league_id']
        league_name = request.form['league_name']
        completed_seasons_num = request.form['completed_seasons_num']

        query = "UPDATE league_histories SET league_name = %s, completed_seasons_num = %s WHERE league_id = %s"
        data = (league_name, completed_seasons_num, league_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/league_histories')

# Seasons READ + CREATE functions
@webapp.route('/seasons', methods=['POST','GET'])
def seasons():
    db_connection = connect_to_database()

    # READ function
    if request.method == 'GET':
        print("Fetching and rendering seasons web page")

        # table data
        query = 'SELECT season_id, league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year from seasons'
        result = execute_query(db_connection, query).fetchall()
        
        # dropdown menu (foreign ID)
        query_a = 'SELECT league_id, league_name from league_histories'
        result_a = execute_query(db_connection, query_a).fetchall()
        
        return render_template("seasons.html", rows=result, rows_a=result_a)

    # CREATE function
    elif request.method == 'POST':
        print("Add new seasons!")
        league_id = request.form['league_id']
        season_name = request.form['season_name']
        date_season_started = request.form['date_season_started']
        date_season_ended = request.form['date_season_ended']
        league_champion = request.form['league_champion']
        western_champion = request.form['western_champion']
        eastern_champion = request.form['eastern_champion']
        most_valuable_player = request.form['most_valuable_player']
        defensive_player_of_the_year = request.form['defensive_player_of_the_year']
        most_improved_player_of_the_year = request.form['most_improved_player_of_the_year']
        sixth_man_of_the_year = request.form['sixth_man_of_the_year']
        
        query = 'INSERT INTO seasons (league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year)
        execute_query(db_connection, query, data)
        
        # table data
        query = 'SELECT season_id, league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year from seasons'
        result = execute_query(db_connection, query).fetchall()

        # dropdown menu (foreign ID)
        query_a = 'SELECT league_id, league_name from league_histories'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("seasons.html", rows=result, rows_a=result_a)

# Seasons DELETE function
@webapp.route('/delete_seasons/<int:season_id>')
def delete_seasons(season_id):
    '''deletes a season with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM seasons WHERE season_id = %s"
    data = (season_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/seasons')

# Seasons UPDATE function
@webapp.route('/update_seasons/<int:season_id>', methods=['POST','GET'])
def update_seasons(season_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # table data
        seasons_query = 'SELECT season_id, league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year from seasons WHERE season_id = %s'  % (season_id)
        seasons_result = execute_query(db_connection, seasons_query).fetchone()

        # dropdown menu (foreign ID)
        query_a = 'SELECT league_id, league_name from league_histories'
        result_a = execute_query(db_connection, query_a).fetchall()

        if seasons_result == None:
            return "No such season found!"

        print('Returning')
        return render_template('update_seasons.html', seasons = seasons_result, rows_a=result_a)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        league_id = request.form['league_id']
        season_name = request.form['season_name']
        date_season_started = request.form['date_season_started']
        date_season_ended = request.form['date_season_ended']
        league_champion = request.form['league_champion']
        western_champion = request.form['western_champion']
        eastern_champion = request.form['eastern_champion']
        most_valuable_player = request.form['most_valuable_player']
        defensive_player_of_the_year = request.form['defensive_player_of_the_year']
        most_improved_player_of_the_year = request.form['most_improved_player_of_the_year']
        sixth_man_of_the_year = request.form['sixth_man_of_the_year']

        query = "UPDATE seasons SET league_id = %s, season_name = %s, date_season_started = %s, date_season_ended = %s, league_champion = %s, western_champion = %s, eastern_champion = %s, most_valuable_player = %s, defensive_player_of_the_year = %s, most_improved_player_of_the_year = %s, sixth_man_of_the_year = %s WHERE season_id = %s"
        data = (league_id, season_name, date_season_started, date_season_ended, league_champion, western_champion, eastern_champion, most_valuable_player, defensive_player_of_the_year, most_improved_player_of_the_year, sixth_man_of_the_year, season_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/seasons')

# Teams SELECT + CREATE function
@webapp.route('/teams', methods=['POST','GET'])
def teams():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering teams web page")
        
        # table data
        query = 'SELECT team_id, season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage from teams'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT season_id, season_name from seasons'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("teams.html", rows=result, rows_a=result_a)
    
    # CREATE function
    elif request.method == 'POST':
        print("Add new teams!")
        season_id = request.form['season_id']
        team_name = request.form['team_name']
        team_place_city = request.form['team_place_city']
        team_place_state = request.form['team_place_state']
        points_per_game = request.form['points_per_game']
        assists_per_game = request.form['assists_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        fouls_per_game = request.form['fouls_per_game']
        fg_attempted_per_game = request.form['fg_attempted_per_game']
        three_pt_fg_attempted_per_game = request.form['three_pt_fg_attempted_per_game']
        ft_attempted_per_game = request.form['ft_attempted_per_game']
        fg_percentage = request.form['fg_percentage']
        three_pt_fg_percentage = request.form['three_pt_fg_percentage']
        ft_percentage = request.form['ft_percentage']
        point_differential = request.form['point_differential']
        reg_season_wins_num = request.form['reg_season_wins_num']
        reg_season_losses_num = request.form['reg_season_losses_num']
        reg_season_win_percentage = request.form['reg_season_win_percentage']

        query = 'INSERT INTO teams (season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage)
        execute_query(db_connection, query, data)

        # table data
        query = 'SELECT team_id, season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage from teams'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table
        query_a = 'SELECT season_id, season_name from seasons'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("teams.html", rows=result, rows_a=result_a)

# Teams DELETE function
@webapp.route('/delete_teams/<int:team_id>')
def delete_teams(team_id):
    '''deletes a team with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM teams WHERE team_id = %s"
    data = (team_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/teams') 

# Teams UPDATE function
@webapp.route('/update_teams/<int:team_id>', methods=['POST','GET'])
def update_teams(team_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # data table
        teams_query = 'SELECT team_id, season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage from teams WHERE team_id = %s'  % (team_id)
        teams_result = execute_query(db_connection, teams_query).fetchone()

        # dropdown menu (foreign ID)
        query_a = 'SELECT season_id, season_name from seasons'
        result_a = execute_query(db_connection, query_a).fetchall()

        if teams_result == None:
            return "No such tean found!"

        print('Returning')
        return render_template('update_teams.html', teams = teams_result, rows_a=result_a)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        season_id = request.form['season_id']
        team_name = request.form['team_name']
        team_place_city = request.form['team_place_city']
        team_place_state = request.form['team_place_state']
        points_per_game = request.form['points_per_game']
        assists_per_game = request.form['assists_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        fouls_per_game = request.form['fouls_per_game']
        fg_attempted_per_game = request.form['fg_attempted_per_game']
        three_pt_fg_attempted_per_game = request.form['three_pt_fg_attempted_per_game']
        ft_attempted_per_game = request.form['ft_attempted_per_game']
        fg_percentage = request.form['fg_percentage']
        three_pt_fg_percentage = request.form['three_pt_fg_percentage']
        ft_percentage = request.form['ft_percentage']
        point_differential = request.form['point_differential']
        reg_season_wins_num = request.form['reg_season_wins_num']
        reg_season_losses_num = request.form['reg_season_losses_num']
        reg_season_win_percentage = request.form['reg_season_win_percentage']

        query = "UPDATE teams SET season_id = %s, team_name = %s, team_place_city = %s, team_place_state = %s, points_per_game = %s, assists_per_game = %s, steals_per_game = %s, blocks_per_game = %s, rebounds_per_game = %s, fouls_per_game = %s, fg_attempted_per_game = %s , three_pt_fg_attempted_per_game = %s , ft_attempted_per_game = %s , fg_percentage = %s , three_pt_fg_percentage = %s , ft_percentage = %s , point_differential = %s , reg_season_wins_num = %s , reg_season_losses_num = %s , reg_season_win_percentage = %s WHERE team_id = %s"
        data = (season_id, team_name, team_place_city, team_place_state, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, point_differential, reg_season_wins_num, reg_season_losses_num, reg_season_win_percentage, team_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/teams')

# Players SELECT + CREATE functions
@webapp.route('/players', methods=['POST','GET'])
def players():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering players web page")

        # table data
        query = 'SELECT player_id, team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus from players'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("players.html", rows=result, rows_a=result_a)
    
    # CREATE function
    elif request.method == 'POST':
        print("Add new players!")
        team_id = request.form['team_id']
        player_name = request.form['player_name']
        player_jersey_number = request.form['player_jersey_number']
        player_height_feet = request.form['player_height_feet']
        player_height_inch = request.form['player_height_inch']
        points_per_game = request.form['points_per_game']
        assists_per_game = request.form['assists_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        fouls_per_game = request.form['fouls_per_game']
        fg_attempted_per_game = request.form['fg_attempted_per_game']
        three_pt_fg_attempted_per_game = request.form['three_pt_fg_attempted_per_game']
        ft_attempted_per_game = request.form['ft_attempted_per_game']
        fg_percentage = request.form['fg_percentage']
        three_pt_fg_percentage = request.form['three_pt_fg_percentage']
        ft_percentage = request.form['ft_percentage']
        plus_minus = request.form['plus_minus']
        
        # Add player entity
        query = 'INSERT INTO players (team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus)
        execute_query(db_connection, query, data)

        # data table
        query = 'SELECT player_id, team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus from players'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("players.html", rows=result, rows_a=result_a)

# Players DELETE function
@webapp.route('/delete_players/<int:player_id>')
def delete_players(player_id):
    '''deletes a player with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM players WHERE player_id = %s"
    data = (player_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/players')   

# Players UPDATE function
@webapp.route('/update_players/<int:player_id>', methods=['POST','GET'])
def update_players(player_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # data table
        players_query = 'SELECT player_id, team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus from players WHERE player_id = %s'  % (player_id)
        players_result = execute_query(db_connection, players_query).fetchone()

        # dropdown menu (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()        

        if players_result == None:
            return "No such player found!"

        print('Returning')
        return render_template('update_players.html', players = players_result, rows_a=result_a)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        team_id = request.form['team_id']
        player_name = request.form['player_name']
        player_jersey_number = request.form['player_jersey_number']
        player_height_feet = request.form['player_height_feet']
        player_height_inch = request.form['player_height_inch']
        points_per_game = request.form['points_per_game']
        assists_per_game = request.form['assists_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        fouls_per_game = request.form['fouls_per_game']
        fg_attempted_per_game = request.form['fg_attempted_per_game']
        three_pt_fg_attempted_per_game = request.form['three_pt_fg_attempted_per_game']
        ft_attempted_per_game = request.form['ft_attempted_per_game']
        fg_percentage = request.form['fg_percentage']
        three_pt_fg_percentage = request.form['three_pt_fg_percentage']
        ft_percentage = request.form['ft_percentage']
        plus_minus = request.form['plus_minus']

        query = "UPDATE players SET team_id = %s, player_name = %s, player_jersey_number = %s, player_height_feet = %s, player_height_inch = %s, points_per_game = %s, assists_per_game = %s, steals_per_game = %s, blocks_per_game = %s, rebounds_per_game = %s, fouls_per_game = %s, fg_attempted_per_game = %s , three_pt_fg_attempted_per_game = %s , ft_attempted_per_game = %s , fg_percentage = %s , three_pt_fg_percentage = %s , ft_percentage = %s , plus_minus = %s WHERE player_id = %s"
        data = (team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus, player_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/players') 

# Players FILTER function
@webapp.route('/filter_players', methods=['POST','GET'])
def filter_players():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering players web page")

        # table data
        query = 'SELECT player_id, team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus from players'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (team name)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("search_players.html", rows=result, rows_a=result_a)
    
    # SELECT function for FILTER function
    elif request.method == 'POST':
        print("Search new players!")
        team_id = request.form['team_id']

        # data table
        query = 'SELECT player_id, team_id, player_name, player_jersey_number, player_height_feet, player_height_inch, points_per_game, assists_per_game, steals_per_game, blocks_per_game, rebounds_per_game, fouls_per_game, fg_attempted_per_game, three_pt_fg_attempted_per_game, ft_attempted_per_game, fg_percentage, three_pt_fg_percentage, ft_percentage, plus_minus FROM players WHERE team_id = %s' % (team_id)
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (team name)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("search_players.html", rows=result, rows_a=result_a)

# Coaches SELECT + CREATE functions
@webapp.route('/coaches', methods=['POST','GET'])
def coaches():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering coaches web page")

        # data table
        query = 'SELECT coach_id, team_id, coach_name, coach_wins, coach_losses, coach_win_percentage from coaches'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()
        
        return render_template("coaches.html", rows=result, rows_a=result_a)

    # CREATE function
    elif request.method == 'POST':
        print("Add new coaches!")
        team_id = request.form['team_id']
        coach_name = request.form['coach_name']
        coach_wins = request.form['coach_wins']
        coach_losses = request.form['coach_losses']
        coach_win_percentage = request.form['coach_win_percentage']

        query = 'INSERT INTO coaches (team_id, coach_name, coach_wins, coach_losses, coach_win_percentage) VALUES (%s,%s,%s,%s,%s)'
        data = (team_id, coach_name, coach_wins, coach_losses, coach_win_percentage)
        execute_query(db_connection, query, data)

        # data table
        query = 'SELECT coach_id, team_id, coach_name, coach_wins, coach_losses, coach_win_percentage from coaches'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()

        return render_template("coaches.html", rows=result, rows_a=result_a)

# Coaches DELETE function
@webapp.route('/delete_coaches/<int:coach_id>')
def delete_coaches(coach_id):
    '''deletes a coach with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM coaches WHERE coach_id = %s"
    data = (coach_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/coaches')   

# Coaches UPDATE function
@webapp.route('/update_coaches/<int:coach_id>', methods=['POST','GET'])
def update_coaches(coach_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # data table
        coaches_query = 'SELECT coach_id, team_id, coach_name, coach_wins, coach_losses, coach_win_percentage from coaches WHERE coach_id = %s'  % (coach_id)
        coaches_result = execute_query(db_connection, coaches_query).fetchone()

        # dropdown menu (foreign ID)
        query_a = 'SELECT team_id, team_name from teams'
        result_a = execute_query(db_connection, query_a).fetchall()   

        if coaches_result == None:
            return "No such coach found!"

        print('Returning')
        return render_template('update_coaches.html', coaches = coaches_result, rows_a=result_a)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        team_id = request.form['team_id']
        coach_name = request.form['coach_name']
        coach_wins = request.form['coach_wins']
        coach_losses = request.form['coach_losses']
        coach_win_percentage = request.form['coach_win_percentage']

        query = "UPDATE coaches SET team_id = %s, coach_name = %s, coach_wins = %s, coach_losses = %s, coach_win_percentage = %s WHERE coach_id = %s"
        data = (team_id, coach_name, coach_wins, coach_losses, coach_win_percentage, coach_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/coaches')

# Player team relations SELECT + CREATE functions
@webapp.route('/player_team_relations', methods=['POST','GET'])
def player_team_relations():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering player_team_relations web page")

        # data table (Inner Join)
        query = 'SELECT player_team_relations.player_team_id, player_team_relations.player_id, players.player_name, player_team_relations.team_id, teams.team_name FROM ((player_team_relations INNER JOIN players ON player_team_relations.player_id = players.player_id) INNER JOIN teams ON player_team_relations.team_id = teams.team_id) '
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT player_id, player_name from players'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()

        return render_template("player_team_relations.html", rows=result, rows_a=result_a, rows_b=result_b)

    # CREATE function 
    elif request.method == 'POST':
        print("Add new player team relationships!")
        player_id = request.form['player_id']
        team_id = request.form['team_id']

        query = 'INSERT INTO player_team_relations (player_id, team_id) VALUES (%s,%s)'
        data = (player_id, team_id)
        execute_query(db_connection, query, data)

        # data table (Inner Join)
        query = 'SELECT player_team_relations.player_team_id, player_team_relations.player_id, players.player_name, player_team_relations.team_id, teams.team_name FROM ((player_team_relations INNER JOIN players ON player_team_relations.player_id = players.player_id) INNER JOIN teams ON player_team_relations.team_id = teams.team_id) '
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT player_id, player_name from players'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()

        return render_template("player_team_relations.html", rows=result, rows_a=result_a, rows_b=result_b)

# Player team relations DELETE function
@webapp.route('/delete_player_team_relations/<int:player_team_id>')
def delete_player_team_relations(player_team_id):
    '''deletes a player team relation with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM player_team_relations WHERE player_team_id = %s"
    data = (player_team_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/player_team_relations')   

# Player team relations UPDATE function
@webapp.route('/update_player_team_relations/<int:player_team_id>', methods=['POST','GET'])
def update_player_team_relations(player_team_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # data table
        player_team_relations_query = 'SELECT player_team_id, player_id, team_id from player_team_relations WHERE player_team_id = %s'  % (player_team_id)
        player_team_relations_result = execute_query(db_connection, player_team_relations_query).fetchone()

        # dropdown table (foreign ID)
        query_a = 'SELECT player_id, player_name from players'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()
        
        if player_team_relations_result == None:
            return "No such coach found!"

        print('Returning')
        return render_template('update_player_team_relations.html', player_team_relations = player_team_relations_result, rows_a=result_a, rows_b=result_b)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        player_team_id = request.form['player_team_id']
        player_id = request.form['player_id']
        team_id = request.form['team_id']

        query = "UPDATE player_team_relations SET player_id = %s, team_id = %s WHERE player_team_id = %s"
        data = (player_id, team_id, player_team_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/player_team_relations')

# Coach team relations SELECT + CREATE functions
@webapp.route('/coach_team_relations', methods=['POST','GET'])
def coach_team_relations():

    db_connection = connect_to_database()

    # SELECT function
    if request.method == 'GET':
        print("Fetching and rendering coach_team_relations web page")

        # data table (Inner Join)
        query = 'SELECT coach_team_relations.coach_team_id, coach_team_relations.coach_id, coaches.coach_name, coach_team_relations.team_id, teams.team_name FROM ((coach_team_relations INNER JOIN coaches ON coach_team_relations.coach_id = coaches.coach_id) INNER JOIN teams ON coach_team_relations.team_id = teams.team_id)'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT coach_id, coach_name from coaches'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()

        return render_template("coach_team_relations.html", rows=result, rows_a=result_a, rows_b=result_b)
    
    # CREATE function
    elif request.method == 'POST':
        print("Add new player team relationships!")
        coach_id = request.form['coach_id']
        team_id = request.form['team_id']

        query = 'INSERT INTO coach_team_relations (coach_id, team_id) VALUES (%s,%s)'
        data = (coach_id, team_id)
        execute_query(db_connection, query, data)
        
        # data table
        query = 'SELECT coach_team_relations.coach_team_id, coach_team_relations.coach_id, coaches.coach_name, coach_team_relations.team_id, teams.team_name FROM ((coach_team_relations INNER JOIN coaches ON coach_team_relations.coach_id = coaches.coach_id) INNER JOIN teams ON coach_team_relations.team_id = teams.team_id)'
        result = execute_query(db_connection, query).fetchall()

        # dropdown table (foreign ID)
        query_a = 'SELECT coach_id, coach_name from coaches'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()

        return render_template("coach_team_relations.html", rows=result, rows_a=result_a, rows_b=result_b)

# Player team relations DELETE function
@webapp.route('/delete_coach_team_relations/<int:coach_team_id>')
def delete_coach_team_relations(coach_team_id):
    '''deletes a coach team relation with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM coach_team_relations WHERE coach_team_id = %s"
    data = (coach_team_id,)

    result = execute_query(db_connection, query, data)
    return redirect('/coach_team_relations')

# Player team relations UPDATE function
@webapp.route('/update_coach_team_relations/<int:coach_team_id>', methods=['POST','GET'])
def update_coach_team_relations(coach_team_id):
    print('In the function')
    db_connection = connect_to_database()

    # SELECT function for UPDATE function
    if request.method == 'GET':
        print('The GET request')

        # data table
        coach_team_relations_query = 'SELECT coach_team_id, coach_id, team_id from coach_team_relations WHERE coach_team_id = %s'  % (coach_team_id)
        coach_team_relations_result = execute_query(db_connection, coach_team_relations_query).fetchone()

        # dropdown table (foreign ID)
        query_a = 'SELECT coach_id, coach_name from coaches'
        result_a = execute_query(db_connection, query_a).fetchall()

        # dropdown table (foreign ID)
        query_b = 'SELECT team_id, team_name from teams'
        result_b = execute_query(db_connection, query_b).fetchall()

        if coach_team_relations_result == None:
            return "No such coach found!"

        print('Returning')
        return render_template('update_coach_team_relations.html', coach_team_relations = coach_team_relations_result, rows_a=result_a, rows_b=result_b)
    
    # UPDATE function
    elif request.method == 'POST':
        print('The POST request')
        coach_team_id = request.form['coach_team_id']
        coach_id = request.form['coach_id']
        team_id = request.form['team_id']

        query = "UPDATE coach_team_relations SET coach_id = %s, team_id = %s WHERE coach_team_id = %s"
        data = (coach_id, team_id, coach_team_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/coach_team_relations')

# 400 error handler
@webapp.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400

# 404 error handler
@webapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# 500 error handler
@webapp.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500
