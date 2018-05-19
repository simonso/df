from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/resource", methods=['GET'])
def get_resource():
    return jsonify({'resource_id': '1111'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8888)
