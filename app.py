import os
from flask import Flask, render_template
from models import db, Vote  # Import the db and Vote model from models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'test'),
    os.getenv('DB_PASSWORD', 'test'),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'flask')
)
db.init_app(app)

@app.route('/')
def index():
    votes = Vote.query.all()
    return render_template('read_votes.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
