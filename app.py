from flask import Flask, jsonify
from flask import request
import json
import main as m
import combinedsearch as c

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/tasks/<string:user_name>', methods=['GET'])
def get_task(user_name):
    return jsonify(m.tasks(user_name))

@app.route('/api/tasks/CombinedSearch/', methods=['GET'])
def combinedSearch():
    bar = request.args.to_dict()
    print(bar)
    username = []
    for index in range(len(bar)):
        username.append(bar[str(index+1)])
    return jsonify(c.combinedsearch(username))

if __name__ == '__main__':
    app.run()
