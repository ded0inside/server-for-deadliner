class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    type = db.Column(db.String(300))
    place = db.Column(db.String(300))
    teacher = db.Column(db.String(300))
    date = db.Column(db.Integer)
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