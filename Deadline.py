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