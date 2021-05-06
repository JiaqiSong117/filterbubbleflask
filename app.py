from flask import Flask, jsonify
from flask import request
import main as m
import combinedsearch as c
import Data_pipeline_v8 as d
import searchash as s

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
    username = []
    for index in range(len(bar)):
        username.append(bar[str(index+1)])
    return jsonify(c.combinedsearch(username))

@app.route('/api/tasks/trending/', methods=['GET'])
def trending():
    return d.trending()

@app.route('/api/tasks/hashtag/<string:hashtag>', methods=['GET'])
def get_hashtag(hashtag):
    return s.hash(hashtag)

if __name__ == '__main__':
    app.run()
