from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('brooklyn_nets.db')
    return conn


@app.route('/')
def index():
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
    cur.execute('SELECT * FROM players')
    players = cur.fetchall()
    conn.close()
    return render_template('players.html', players=players)


@app.route('/stats')
def stats():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM overall_stats').fetchall()
    conn.close()
    return render_template('stats.html', stats=stats)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    cur = conn.cursor()
    #game_information = conn.execute("SELECT * FROM game_information WHERE player_id LIKE ?", ('%' + query + '%',)).fetchall()
    players = cur.execute("SELECT * FROM players WHERE first_name LIKE ?", ('%' + query + '%',)).fetchall()
    print(players)
    conn.close()
    return render_template('search_results.html', query=query, players=players)


if __name__ == '__main__':
    app.run(debug=True)