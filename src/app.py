from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {"label": "Terminar puzzler", "done": False},
    {"label": "Repasar hindi", "done": False}
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)  
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
    else:
        return jsonify({"error": "Invalid position"}), 400
    return jsonify(todos)

#the code below should always be at the end of the app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)