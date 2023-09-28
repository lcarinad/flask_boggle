from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)


from boggle import Boggle
app.config['SECRET_KEY'] = 'abc123'

boggle_game = Boggle()

@app.route('/')
def index():
    new_board = Boggle()
    board = new_board.make_board()
    return render_template('index.html', board = board)
