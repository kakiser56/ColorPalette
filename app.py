import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
            template_folder='templates')
@app.route("/")
def index():
    return "Hello from flask!"

if __name__ == "__main__":
    app.run(debug=True)
