from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.String, index=True, unique=False)
    date = db.Column(db.String)

    def __repr__(self):
        return '<User {} scanned at {}>'.format(self.card_id, self.date)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))