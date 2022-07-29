from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import os
from flask import Flask, Response, render_template, request, json
from dotenv import load_dotenv
import re

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
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
    "travel" : "/static/img/travel.jpeg",
    "jwst" : "/static/img/jwst.png",
    "patrick_and_gary" : "/static/img/patrick_and_gary.png",
    "pc_setup" : "/static/img/pc_setup.png",
    "r2-d2" : "/static/img/r2-d2.png",
    "RoyalGameOfUr_1" : "/static/img/RoyalGameOfUr_1.png",
    "radium_utahTeapot" : "/static/img/radium_utahTeapot.png",
    "sling" : "/static/img/sling.jpg",
    "sheetmusic" : "/static/img/sheetmusic.png",
    "ai_racers2" : "/static/img/ai_racers2.png",
    "vbot2" : "/static/img/vbot2.png",
    "diceleaffin" : "/static/img/diceleaffin.png",
    "ai_racers" : "/static/img/ai_racers.png",
    "keysandlocks" : "/static/img/keysandlocks.png",
    "space_sim" : "/static/img/space_sim.png",
    "calligraphy" : "/static/img/calligraphy.png"
}

#fixing warning:  Enable tracemalloc to get the object allocation traceback
footerF = open("./app/static/footer.json")
footerJson = json.load(footerF)
footerF.close()

landingF = open("./app/static/landingPage.json")
landing = json.load(landingF)
landingF.close()

workF = open("./app/static/work_edu.json")
workJson = json.load(workF)
workF.close()

hobbiesF = open("./app/static/hobbies.json")
hobbiesJson = json.load(hobbiesF)
hobbiesF.close()

@app.route('/')
def index():
    
    return render_template(
        'landingPage.html', 
        images = images,
        data = landing,
        info = footerJson["FooterInformation"],
        url = os.getenv("URL")
    )

@app.route('/work')
def work():
    data = workJson
    footer = footerJson
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
    datahobbies = hobbiesJson
    footer = footerJson
    return render_template(
        'hobbies.html',
        images = images,
        data = datahobbies,
        hobbies = datahobbies["Hobbies"],
        map_hobbies = datahobbies["Map"],
        conclusion = datahobbies["Conclusion"],
        info = footer["FooterInformation"],
    )

@app.route('/timeline')
def timeline():
    datahobbies = hobbiesJson
    footer = footerJson
    return render_template(
        'timeline.html',
        images = images,
        data = datahobbies,
        hobbies = datahobbies["Hobbies"],
        conclusion = datahobbies["Conclusion"],
        info = footer["FooterInformation"],
    )

@app.route('/projects')
def projects():
    datahobbies = hobbiesJson
    footer = footerJson
    return render_template(
        'projects.html',
        images = images,
        data = datahobbies,
        hobbies = datahobbies["Hobbies"],
        map_hobbies = datahobbies["Map"],
        conclusion = datahobbies["Conclusion"],
        info = footer["FooterInformation"],
    )

# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html',title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():

    try:
        name = request.form['name']
        if name == '': raise Exception()
    except:
        return "Invalid name", 400
    
    try:
        email = request.form['email']
        if email == '' or not re.match('[^@]+@[^@]+\.[^@]+',email): raise Exception()
    except:
        return "Invalid email", 400
    
    try:
        content = request.form['content']
        if content == '': raise Exception()
    except:
        return "Invalid content", 400

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