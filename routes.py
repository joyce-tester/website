from flask import render_template, request, redirect, url_for
from app import app
#from website.bk.models import User, Course, WeeklyTopic, Project, Submission

@app.route("/")
def homepage():
   # courses = Course.query.all()
    return render_template("home.html")
@app.route('/python')
def python():
    return render_template('python.html')  # You can create a separate HTML file for this page
@app.route('/java')
def java():
    return render_template('java.html')  
# @app.route("/course/<int:course_id>")
# def course_detail(course_id):
#     topics = WeeklyTopic.query.filter_by(course_id=course_id).all()
#     return render_template("course_detail.html", topics=topics)

# @app.route("/project/<int:topic_id>")
# def project_detail(topic_id):
#     project = Project.query.filter_by(topic_id=topic_id).first()
#     return render_template("project_detail.html", project=project)
