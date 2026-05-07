from flask import Flask, render_template
import mysql.connector
from game_data import cover_images, youtube_links, long_descriptions
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

app = Flask(__name__)

def get_videogames():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="videogames_review"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM videogames")
    videogames = cursor.fetchall()
    cursor.close()
    conn.close()

    for game in videogames:
        game['image_url'] = cover_images.get(game['nome'], 'https://via.placeholder.com/200x120?text=No+Image')
        game['youtube'] = youtube_links.get(game['nome'], '')
        game['description'] = long_descriptions.get(game['nome'], "Descrizione non disponibile")

    return videogames

@app.route("/")
def homepage():
    videogames = get_videogames()
    return render_template("videogames.html", videogames=videogames)

@app.route("/game/<nome>")
def game_detail(nome):
    videogames = get_videogames()
    nome_norm = nome.lower().replace(' ', '')
    game = next((g for g in videogames if g['nome'].lower().replace(' ', '') == nome_norm), None)
    if not game:
        return "Il gioco non è stato trovato", 404
    return render_template("game_detail.html", game=game)

if __name__ == "__main__":
    app.run(debug=True)