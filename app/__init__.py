from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print("firstprint",mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

images = {
    "logo": "/static/img/logo.svg",
    "profilePic" : "/static/img/logo.jpg",
    "desk" : "/static/img/desk_background.jpg",
    "travel" : "/static/img/travel.jpeg"
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
        'hobbies.html',
        images = images,
        data = data,
        hobbies = data["Hobbies"],
        conclusion = data["Conclusion"],
        info = footer["FooterInformation"],
    )

@app.route('/timeline')
def timeline():
    data = json.load(open("./app/static/hobbies.json"))
    footer = json.load(open("./app/static/footer.json"))
    return render_template(
        'timeline.html',
        images = images,
        data = data,
        hobbies = data["Hobbies"],
        conclusion = data["Conclusion"],
        info = footer["FooterInformation"],
    )

# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html',title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(
        name=name,
        email=email,
        content=content
    )

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }