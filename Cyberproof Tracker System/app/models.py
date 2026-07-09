# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Relationship to issues
    issues = db.relationship('Issue', backref='project', lazy=True)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), nullable=False) # e.g., 'Critical', 'Low'
    status = db.Column(db.String(20), default='Open')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)