from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv

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
    "travel" : "/static/img/travel.jpeg"
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