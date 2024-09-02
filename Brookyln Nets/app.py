from flask import Flask, render_template, request
import sqlite3
# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)


# Function to establish a connection to the SQLite database
def get_db_connection():
    # Connect to the 'brooklyn_nets.db' SQLite database and return the connection object.
    conn = sqlite3.connect('brooklyn_nets.db')
    conn = sqlite3.connect('brooklyn_nets.db')
    return conn


# Define a route for the homepage ('/') of the application.
@app.route('/')
def index():
    # Render and return the 'index.html' template when the homepage is accessed.
    return render_template('index.html')


@app.route('/game_info')
def game_info():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM game_information')
    game_information = cur.fetchall()
    conn.close()
    return render_template('game_info.html', game_information=game_information)


@app.route('/players')
def players():
    conn = get_db_connection()
    cur = conn.cursor()
    players = cur.execute('SELECT * FROM players').fetchall()
    conn.close()
    return render_template('players.html', players=players)


@app.route('/stats')
def stats():
    conn = get_db_connection()
    cur = conn.cursor()
    stats = cur.execute('SELECT * FROM overall_stats').fetchall()
    conn.close()
    return render_template('stats.html', stats=stats)


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