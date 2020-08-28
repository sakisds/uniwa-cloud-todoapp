from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html.j2')


def serve():
    app.run(debug=True, host='0.0.0.0', port=5000)
