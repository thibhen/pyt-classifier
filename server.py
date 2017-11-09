#!flask/bin/python
from flask import Flask, jsonify, request
from classify import classify
from update import updateTraining

app = Flask(__name__)


@app.route('/api/classify', methods=['GET'])
def classify_message():
    message = request.args.get('message')
    tags = classify( message )
    return jsonify({'message': message , 'tags' : tags})
    
@app.route('/api/update', methods=['POST'])
def update():
    request_json = request.get_json()
    message = request_json.get('message')
    tag = request_json.get('tag')
    ret = updateTraining(message,tag)
    return jsonify({'status': ret})

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')
