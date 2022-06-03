import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

images ={
    "logo": "/static/img/logo.svg",
    "profilePic" : "/static/img/michael.jpg"
}
@app.route('/')
def index():
    return render_template(
        'landingPage.html', 
        title     = "MLH Fellow",
        images    = images,
        url       = os.getenv("URL")
    )

@app.route('/work')
def work():
    return render_template(
        'Work-Education.html',
        images    = images,

    )
