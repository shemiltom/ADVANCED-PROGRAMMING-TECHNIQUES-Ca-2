from flask import request, jsonify
from models import db, Issue

def register_routes(app):
    
    @app.route('/issues', methods=['POST'])
    def add_issue():
        data = request.get_json()
        new_issue = Issue(
            title=data['title'],
            description=data['description'],
            priority=data['priority'],
            project_id=data['project_id']
        )
        db.session.add(new_issue)
        db.session.commit()
        return jsonify({"message": "Issue added successfully"}), 201

    @app.route('/issues', methods=['GET'])
    def get_issues():
        issues = Issue.query.all()
        return jsonify([{'id': i.id, 'title': i.title, 'priority': i.priority} for i in issues])
    

    @app.route('/issues/<int:id>', methods=['PUT'])
    def update_issue(id):
        issue = Issue.query.get_or_404(id)
        data = request.get_json()
        issue.status = data.get('status', issue.status)
        db.session.commit()
        return jsonify({"message": "Issue updated successfully"})

    @app.route('/issues/<int:id>', methods=['DELETE'])
    def delete_issue(id):
        issue = Issue.query.get_or_404(id)
        db.session.delete(issue)
        db.session.commit()
        return jsonify({"message": "Issue deleted successfully"})