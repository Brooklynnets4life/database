from flask import Flask, render_template, request
import sqlite3 
app = Flask(__name__)


# Initialize the Flask app
def get_db_connection():
    conn = sqlite3.connect('brooklyn_nets.db')
    conn = sqlite3.connect('brooklyn_nets.db')
    return conn


# Function to connect to the database
@app.route('/')
def index():
    return render_template('index.html') 


# Route for game info
@app.route('/game_info')
def game_info():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM game_information').fetchall()
    game_information = cur.fetchall()
    conn.close()
    print("Game Information:", game_information)  # Debug print
    return render_template('game_info.html', game_information=game_information)


# Route for players info
@app.route('/players')
def players():
    conn = get_db_connection()
    cur = conn.cursor()
    players = cur.execute('SELECT * FROM players').fetchall()
    conn.close()
    return render_template('players.html', players=players)


# Route for stats info
@app.route('/stats')
def stats():
    conn = get_db_connection()
    cur = conn.cursor()
    stats = cur.execute('SELECT * FROM overall_stats').fetchall()
    conn.close()
    return render_template('stats.html', stats=stats)


# Route for the search bar
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    cur = conn.cursor()
    players = cur.execute("SELECT * FROM players WHERE name LIKE ?", ('%' + query + '%',)).fetchall()
    print(players)
    conn.close()
    return render_template('search_results.html', query=query, players=players)


# route for 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)