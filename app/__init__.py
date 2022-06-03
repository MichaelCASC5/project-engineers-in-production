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
    jobs = [
        ["/static/img/Work_Education/Job1.jpeg","Major League Hacking","Production Engineer Fellow", "This is a description of what I did in this job", "June 2022 - August 2022"],
    ]

    education = [
        ["/static/img/Work_Education/Job1.jpeg","Major League Hacking","Pre Fellow", "This is a description of what I did in this job", "April 2022"],
        ["static/img/Work_Education/Edu1.jpeg", "Tec de Monterrey","BS. in Robotic and Digital Systems"],
    ]
    return render_template(
        'Work-Education.html',
        images    = images,
        jobs = jobs,
        education = education

    )
