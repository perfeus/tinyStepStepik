import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    sample = random.sample(lst, 6)
    with open("teachers.json", "r", encoding="utf-8") as db:
        teachers = json.loads(db.read())

    return render_template("index.html", sample=sample, teachers=teachers)


@app.route("/all/")
def allTeachers():
    return render_template("all.html")


@app.route("/goals/<goal>/")
def allGoals(goal):
    with open("goals.json", "r", encoding="utf-8") as db:
        goals = json.loads(db.read())

    with open("teachers.json", "r", encoding="utf-8") as db:
        teachers = json.loads(db.read())
    return render_template("goal.html", goal=goal, goals=goals, teachers=teachers)


@app.route("/profiles/<int:id>/")
def idTeacher(id):
    with open("teachers.json", "r", encoding="utf-8") as db:
        teachers = json.loads(db.read())
    # id = int(id)
    return render_template("profile.html", id=id, teachers=teachers)


@app.route("/request/")
def requestSelect():
    return "Here is going to be a request to select"


@app.route("/request_done/")
def requestDone():
    return "Here is going to be a select request is sent"


@app.route("/booking/<id>/<weekDay>/<time>/")
def bookingForm(id, weekDay, time):
    with open("teachers.json", "r", encoding="utf-8") as db:
        teachers = json.loads(db.read())
    id = int(id)
    return render_template("booking.html", id=id, weekDay=weekDay, time=time, teachers=teachers)


@app.route("/booking_done/", methods=["POST"])
def bookingDone():
    clientData = {
        "clientDay": None,
        "clientTime": None,
        "clientTeacher": None,
        "clientName": None,
        "clientPhone": None
    }
    if request.method == "POST":
        clientWeekDay = request.form["clientWeekday"]
        clientData["clientDay"] = clientWeekDay
        clientTime = request.form["clientTime"]
        clientData["clientTime"] = clientTime
        clientTeacher = request.form["clientTeacher"]
        clientData["clientTeacher"] = clientTeacher
        clientName = request.form["clientName"]
        clientData["clientName"] = clientName
        clientPhone = request.form["clientPhone"]
        clientData["clientPhone"] = clientPhone
        print(request.form, clientWeekDay, clientData, sep="\n")
        with open("request.json", "r", encoding="utf-8") as f:
            record = json.load(f)
            record.append(clientData)
            with open("request.json", "w", encoding="utf-8") as f:
                json.dump(record,
                          f,
                          ensure_ascii=False,
                          sort_keys=True,
                          indent=2,
                          separators=(',', ': '))
        return render_template("booking_done.html", clientWeekDay=clientWeekDay,
                               clientTime=clientTime, clientTeacher=clientTeacher,
                               clientName=clientName, clientPhone=clientPhone)
    else:
        return "There are no data to render"


if __name__ == "__main__":
    app.run(debug=True)
