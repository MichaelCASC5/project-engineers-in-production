import os
from flask import Flask, render_template, request, json
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
        images = images,
        data = json.load(open("./app/static/landingPage.json")),
        url = os.getenv("URL")
    )

@app.route('/work')
def work():
    data = json.load(open("./app/static/work_edu.json"))
    return render_template(
        'Work-Education.html',
        images    = images,
        jobs = data["Work experience"],
        education = data["Education"]

    )
@app.route('/hobbies')
def hobbies():
    return render_template(
        'Hobbies.html',
        images = images
    )
