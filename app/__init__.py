import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
images ={
    "logo": "/static/img/logo.svg",
    "profilePic" : "/static/img/logo.jpg"
}

@app.route('/')
def index():
    footer = json.load(open("./app/static/footer.json"))
    return render_template(
        'landingPage.html', 
        images = images,
        data = json.load(open("./app/static/landingPage.json")),
        info = footer["FooterInformation"],
        url = os.getenv("URL")
    )

@app.route('/work')
def work():
    data = json.load(open("./app/static/work_edu.json"))
    footer = json.load(open("./app/static/footer.json"))
    return render_template(
        'Work-Education.html',
        images    = images,
        jobs = data["Work experience"],
        education = data["Education"],
        skills = data["Skills"],
        info = footer["FooterInformation"],
    )

@app.route('/hobbies')
def hobbies():
    data = json.load(open("./app/static/hobbies.json"))
    footer = json.load(open("./app/static/footer.json"))
    return render_template(
        'Hobbies.html',
        images = images,
        data = data,
        hobbies = data["Hobbies"],
        info = footer["FooterInformation"],
    )
