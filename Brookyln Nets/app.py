from flask import Flask, render_template, request  # Import Flask and necessary modules
import sqlite3  #Import SQLite3 for database connections
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
    cur.execute('SELECT * FROM game_information')
    game_information = cur.fetchall()
    conn.close()
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


if __name__ == '__main__':
    app.run(debug=True)