from flask import Flask, render_template, request, redirect, session, jsonify



app = Flask(__name__)


from boggle import Boggle
app.config['SECRET_KEY'] = 'abc123'

boggle_game = Boggle()

@app.route('/')
def index():
    new_board = Boggle()
    board = new_board.make_board()
    session['current_board'] = board
    return render_template('index.html', board = board)

@app.route('/word', methods=["POST"])
def accept_word():
    submitted_word = request.json.get("word")
    print("************************")
    print(submitted_word)
    return redirect('/')