from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def hello_world():
    todos_json=jsonify(todos)
    return todos_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    todos_json=jsonify(todos)
    print("Incoming request with the following body", request_body)
    return todos_json

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    todos_json=jsonify(todos)
    print("This is the position to delete:", position)
    return todos_json

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

