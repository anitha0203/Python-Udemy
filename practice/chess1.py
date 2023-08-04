from flask import Flask, render_template
from python_chess import Board, Piece

app = Flask(__name__)


@app.route("/")
def index():
    board = Board()
    return render_template("index.html", board=board)


if __name__ == "__main__":
    app.run(debug=True)
