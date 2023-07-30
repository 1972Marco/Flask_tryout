from flask import Flask 
app=Flask(__name__)

@app.route('/')
def home():
    return "<Tekst naar keuze 1 > Hello world! <Tekst naar keuze 2>"
