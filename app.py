from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.debug = True

