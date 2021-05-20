from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    type = db.Column(db.String(300))
    place = db.Column(db.String(300))
    teacher = db.Column(db.String(300))
    date = db.Column(db.String(200))
    how_often = db.Column(db.Integer)

    def __repr__(self):
        return '<Schedule %r>' % self.id

    def to_dict_schedule(self):
        data = {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'place': self.place,
            'teacher': self.teacher,
            'date': self.date,
            'how_often': self.how_often
        }
        return data


class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(300))
    description = db.Column(db.String(300))
    date = db.Column(db.String(10))

    def __repr__(self):
        return '<Deaedline %r>' % self.id

    def to_dict_deadlines(self):
        data = {
            'id': self.id,
            'subject': self.subject,
            'description': self.description,
            'date': self.date,
        }
        return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get-schedule", methods=["GET"])
def get_schedule():
    subjects_list = []
    data = Schedule.query.all()

    for subject in data:
        subjects_list.append(subject.to_dict_schedule())

    return jsonify(subjects_list)


@app.route("/get-deadlines", methods=["GET"])
def get_deadlines():
    subjects_list = []
    data = Deadline.query.all()

    for subject in data:
        subjects_list.append(subject.to_dict_deadlines())

    return jsonify(subjects_list)


@app.route('/create-schedule', methods=['POST', 'GET'])
def create_schedule():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        place = request.form['place']
        teacher = request.form['teacher']
        date = request.form['date']
        how_often = request.form['how_often']

        d = date.split('-')
        print(d)
        day = int(d[2])
        month = int(d[1])
        year = int(d[0])
        date_in_datetime = datetime(year, month, day)
        unix_time = time.mktime(date_in_datetime.timetuple())

        schedule = Schedule(name=name, type=type, place=place, date=unix_time, teacher=teacher, how_often=int(how_often))

        try:
            db.session.add(schedule)
            db.session.commit()
            return redirect('/')

        except:
            return 'Something goes wrong'
    else:
        return render_template('create-schedule.html')


@app.route('/create-deadlines', methods=['POST', 'GET'])
def create_deadlines():
    if request.method == 'POST':
        subject = request.form['subject']
        description = request.form['description']
        date = request.form['date']

        deadline = Deadline(subject=subject, description=description,date=date)

        try:
            db.session.add(deadline)
            db.session.commit()
            return redirect('/')

        except:
            return 'Something goes wrong'
    else:
        return render_template('create-deadlines.html')


@app.route('/schedule')
def schedule():

    schedule = Schedule.query.all()

    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
