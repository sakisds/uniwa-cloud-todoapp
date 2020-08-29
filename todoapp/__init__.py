from datetime import datetime, date

from flask import Flask, render_template, request, redirect
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
    date_completed = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET'])
def index():
    '''
    Returns the main app screen filled with any created tasks.
    '''
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html.j2', tasks=tasks)


@app.route('/', methods=['POST'])
def handle_form():
    '''
    Creates a new task on form submission
    '''
    content = request.form['content']
    task = Todo(content=content)
    try:
        db.session.add(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'Something went wrong! :('


@app.route('/complete/<int:id>')
def complete(id):
    '''Marks a task done by the ID'''
    task = Todo.query.get_or_404(id)
    try:
        task.date_completed = datetime.utcnow()
        db.session.commit()
        return redirect('/')
    except:
        return 'Something went wrong! :('


@app.route('/uncomplete/<int:id>')
def uncomplete(id):
    '''Marks a task undone by the ID'''
    task = Todo.query.get_or_404(id)
    try:
        task.date_completed = None
        db.session.commit()
        return redirect('/')
    except:
        return 'Something went wrong! :('


@app.route('/delete/<int:id>')
def delete(id):
    '''Deletes a task'''
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'Something went wrong! :('


def serve():
    app.run(debug=True, host='0.0.0.0', port=5000)
