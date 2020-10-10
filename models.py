from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    siege_weapon = db.Column(db.String())
    HP = db.Column(db.String())

    def __init__(self, siege_weapon, HP):
        self.siege_weapon = siege_weapon
        self.HP = HP

    def __repr__(self):
        return '<id {}>'.format(self.id)
