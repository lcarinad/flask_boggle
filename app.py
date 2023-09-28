from flask import Flask, render_template, request, redirect, session

from boggle import Boggle

boggle_game = Boggle()


app = Flask(__name__)