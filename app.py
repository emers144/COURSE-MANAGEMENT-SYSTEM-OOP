from flask import Flask, render_template, request, redirect, url_for
from service import SchoolCMSService

app = Flask(__name__)
cms = SchoolCMSService()

@app.route("/")
def index():
    courses = cms.get_all_courses()
    return render_template("index.html", courses=courses, cms=cms)

@app.route("/add_course", methods=["POST"])
def add_course():
    title = request.form.get("title", "").strip()
    instructor = request.form.get("instructor", "").strip()
    section = request.form.get("section", "").strip()
    if title and instructor and section:
        cms.add_course(title, instructor, section)
    return redirect(url_for("index"))

@app.route("/enroll_student", methods=["POST"])
def enroll_student():
    course_id = request.form.get("course_id", type=int)
    student_name = request.form.get("student_name", "").strip()
    student_id = request.form.get("student_id", "").strip()
    if course_id and student_name and student_id:
        cms.enroll_student(course_id, student_name, student_id)
    return redirect(url_for("index"))

@app.route("/delete_course/<int:course_id>")
def delete_course(course_id):
    cms.delete_course(course_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    # For development only; in production use a proper WSGI server
    app.run(debug=True)
