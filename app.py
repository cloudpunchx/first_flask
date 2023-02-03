from flask import Flask
import json
from dbhelpers import run_statement

# the Name part is a fundamental of flask, not a variable, no reason to ever change this
app = Flask(__name__)

@app.get('/hello')
def get_hello():
    return "Hello World"

@app.post('/hello')
def post_hello():
    return "Hello Again"

@app.get('/homes')
def get_homes():
    result = run_statement("CALL room_filter_search(?)", [1])
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else: 
        return "Sorry, something went wrong."


app.run(debug = True)