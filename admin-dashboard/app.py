# Flask admin dashboard starter
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    print(data)
    return jsonify({'status': 'received'})
