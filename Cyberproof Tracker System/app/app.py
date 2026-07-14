# app.py
from flask import Flask, render_template
from sqlalchemy import text
from models import db
from routes import register_routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyberproof.db'
db.init_app(app)

register_routes(app)

@app.route('/')
def home():
    return text("hello")

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)