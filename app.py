from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to our API!"}), 200

@app.route('/api/data', methods=['GET'])
def return_data():
    data = {"Name": "John", "Age": 30, "Job": "Engineer"}  
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
