from flask import Flask, render_template, request, redirect, session, jsonify, flash

app = Flask(__name__)

from boggle import Boggle
app.config['SECRET_KEY'] = 'abc123'

boggle_game = Boggle()

@app.route('/')
def index():
    board = boggle_game.make_board()
    session['current_board'] = board 
    return render_template('index.html', board = board)

@app.route('/word', methods=["POST"])
def accept_word():
    # import pdb
    # pdb.set_trace()
   
    submitted_word = request.json.get("word")   
    result =  boggle_game.check_valid_word(session['current_board'], submitted_word)
    
    response = jsonify({"result":result})

    return response
    
@app.route('/end', methods=["POST"])
def update():
    score = request.json.get("score")
    if "player_scores" in session:
        session["player_scores"].append(score)
    else:
        session['player_scores']=[score]

    
    if "num_game_played" in session:
        session["num_game_played"] = session.get("num_game_played")+1
    else:
        session["num_game_played"] = 1
    
    return redirect("/")