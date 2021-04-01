from flask import Flask, jsonify
import main as m

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/tasks/<string:user_name>', methods=['GET'])
def get_task(user_name):
    return jsonify(m.tasks(user_name))


if __name__ == '__main__':
    app.run()
