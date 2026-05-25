from flask import Flask, request, jsonify
from app.tasks import add_task, get_tasks, delete_task, mark_complete

app = Flask(__name__)

@app.route("/")
def home():
    return "Task Manager API Running!"

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    title = data.get("title")
    priority = data.get("priority", "medium")

    add_task(title, priority)

    return jsonify({
        "message": "Task added!"
    })

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)

    return jsonify({
        "message": "Task deleted!"
    })

@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def complete_task(task_id):
    mark_complete(task_id)

    return jsonify({
        "message": "Task completed!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)