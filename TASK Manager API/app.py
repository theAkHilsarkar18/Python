# pip install Flask Flask-RESTful Flask-SQLAlchemy

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    assign_by = db.Column(db.String(80), nullable=False)
    assign_to = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'priority': self.priority,
            'assign_by': self.assign_by,
            'assign_to': self.assign_to,
            'date': self.date.isoformat(),
            'description': self.description
        }

with app.app_context():
    db.create_all()

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    def post(self):
        data = request.get_json()
        new_task = Task(
            name=data['name'],
            priority=data['priority'],
            assign_by=data['assign_by'],
            assign_to=data['assign_to'],
            date=datetime.fromisoformat(data['date']),
            description=data.get('description', '')
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return jsonify(task.to_dict())

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.name = data['name']
        task.priority = data['priority']
        task.assign_by = data['assign_by']
        task.assign_to = data['assign_to']
        task.date = datetime.fromisoformat(data['date'])
        task.description = data.get('description', '')
        db.session.commit()
        return jsonify(task.to_dict())

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    

# Example data input format

# {
#     "name": "Updated Task Name",
#     "priority": "Low",
#     "assign_by": "Alice",
#     "assign_to": "Charlie",
#     "date": "2024-07-19T00:00:00",
#     "description": "Updated task description"
# }

# Website : http://192.168.29.41:5000