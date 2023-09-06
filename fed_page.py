from flask import Flask, render_template
import json

app = Flask(__name__)

# Sample JSON data
with open('FEDMonitor_2023_09_01_v2.json', 'r') as json_file:
    data = json.load(json_file)
@app.route('/')
def index():
    return render_template('index_work.html', data=data['table']['rows'], headers=data['table']['definition'])

if __name__ == '__main__':
    app.run(debug=True)