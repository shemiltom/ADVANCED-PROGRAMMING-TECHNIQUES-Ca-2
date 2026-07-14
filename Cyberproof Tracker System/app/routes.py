from flask import request, jsonify
from models import db, Issue, Project

def register_routes(app):
    @app.route('/projects', methods=['POST'])
    def add_project():
        data = request.get_json()
        new_project = Project(
            name=data['name'],
            description=data['description']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project created successfully", "id": new_project.id})

    @app.route('/projects', methods=['GET'])
    def get_projects():
        projects = Project.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'description': p.description} for p in projects])
    
    @app.route('/projects/<int:id>', methods=['DELETE'])
    def delete_project(id):
        project = Project.query.get_or_404(id)
        for issue in project.issues:
            db.session.delete(issue)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project and all associated issues are deleted"})
    
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
        return jsonify({"message": "Issue added successfully"})
    
    @app.route('/issues', methods=['GET'])
    def get_issues():
        search = request.args.get('search')
        sort = request.args.get('sort')
        status_filter = request.args.get('status')
        priority_filter = request.args.get('priority')

        query = Issue.query

        if search:
            query = query.filter(Issue.title.ilike(f'%{search}%') | Issue.description.ilike(f'%{search}%'))

        if status_filter:
            query = query.filter(Issue.status == status_filter)
        if priority_filter:
            query = query.filter(Issue.priority == priority_filter)

        if sort == 'createddate':
            query = query.order_by(Issue.createddate.asc())    
        issues = query.all()
        return jsonify([{'id': i.id, 'title': i.title, 'priority': i.priority, 'status': i.status, 'createddate': i.createddate} for i in issues])

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