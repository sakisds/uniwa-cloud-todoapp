from datetime import datetime, date

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To surpress warning
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    date_completed = db.Column(db.DateTime, default=date(2000, 1, 1))

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route("/")
def root():
    return render_template('index.html.j2')


def serve():
    app.run(debug=True, host='0.0.0.0', port=5000)
