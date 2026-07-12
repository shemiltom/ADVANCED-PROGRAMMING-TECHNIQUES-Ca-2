from flask import request, jsonify
from models import db, Issue

def register_routes(app):
    
    @app.route('/issues', methods=['POST'])
    def add_issue():
        data = request.get_json()
        new_issue = Issue(
            title=data['title'],
            description=data['description'],
            severity=data['severity'],
            project_id=data['project_id']
        )
        db.session.add(new_issue)
        db.session.commit()
        return jsonify({"message": "Issue tracked successfully"}), 201

    @app.route('/issues', methods=['GET'])
    def get_issues():
        issues = Issue.query.all()
        return jsonify([{'id': i.id, 'title': i.title, 'severity': i.severity} for i in issues])
    
    # Update an issue status
    @app.route('/issues/<int:id>', methods=['PUT'])
    def update_issue(id):
        issue = Issue.query.get_or_404(id)
        data = request.get_json()
        issue.status = data.get('status', issue.status)
        db.session.commit()
        return jsonify({"message": "Issue updated"})

# Delete an issue
    @app.route('/issues/<int:id>', methods=['DELETE'])
    def delete_issue(id):
        issue = Issue.query.get_or_404(id)
        db.session.delete(issue)
        db.session.commit()
        return jsonify({"message": "Issue deleted"})