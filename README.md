# Cyberproof Tracker System

## 1. Project Overview
The **Cyberproof Tracker System** is a tool that provides a  vulnerability and issue tracking application. It to plan projects, record issues. The system has been built with utmost data integrity, the backend being made of Flask and the front end being dynamic for live interaction.

## 2. Requirements & Implementation
Manages SQLite database with SQLAlchemy (ORM).
Relational mapping – Projects ↔ Issues.
deletes (when deleting a project, issues are deleted, too).
Server-side search and filtering for issues


## 3. How the System Works
Models (models.py) -- the data structure (tables for Projects and Issues).
Routes (routes.py): handles the "waiter" role by accepting requests from the front end and running the commands in the database.
The engine that launches the server and initializes the database is called App (app.py).


## 4. API Documentation (Postman)
To test this system, set your Postman requests as follows:

| Request | Method | Endpoint | Note |
| :--- | :--- | :--- | :--- |
| **Add Project** | POST | `/projects` | Requires JSON: `{name, description}` |
| **Get Projects** | GET | `/projects` | Returns list of projects |
| **Add Issue** | POST | `/issues` | Requires JSON: `{title, description, priority, project_id}` |
| **Get Issues** | GET | `/issues` | Supports `?search=` and `?status=` parameters |
| **Resolve Issue**| PUT | `/issues/<id>` | Updates status to "Resolved" |
| **Delete** | DELETE | `/issues/<id>` | Removes record from database |

## 5. Installation
1. Clone: `git clone [YOUR_GITHUB_LINK]`
2. Install: `pip install flask flask-sqlalchemy`
3. Run: `python app.py`
4. Access: `http://127.0.0.1:5000`

---

## 6. Summary of Code Attributions
In accordance with assessment requirements, all logic origins are disclosed below.

| File / Component | Source | Attribution |
| :--- | :--- | :--- |
| `app.py` | Self| System initialization and context. |
| `models.py` | Self| ORM definitions and relationship mappings. |
| `routes.py` | Self| RESTful endpoint logic and validation. |
| `templates/index.html` | Self |simple html testing need to done in postman|
| `README.md` | Self | Documentation and summary. |

