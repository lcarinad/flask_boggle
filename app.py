from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)


from boggle import Boggle
app.config['SECRET_KEY'] = 'abc123'

boggle_game = Boggle()

@app.route('/')
def index():
    
    return render_template('index.html')
