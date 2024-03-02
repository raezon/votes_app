import os
import json
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Vote  # Import the db and Vote model from models.py


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'test'),
    os.getenv('DB_PASSWORD', 'test'),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'flask')
)
db.init_app(app)


# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('write_vote.html')

@app.route('/write_vote', methods=['POST'])
def write_vote():
    print(request.form)
    name = request.form['name']
    choice = request.form['choice']
    vote = Vote(name=name, choice=choice)
    db.session.add(vote)
    db.session.commit()
    return 'Vote written successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
