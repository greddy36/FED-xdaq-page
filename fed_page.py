from flask import Flask, render_template
import json

app = Flask(__name__)
#Caleb's funtions----------------------------------
def isPixFED(row):
    answer = "PIX FED "
    board_code = row["BoardCode"]
    if board_code == answer:
        return True
    else:
        return False
		
# process data
def process_data(input_data):
    output_data = []
    for row in input_data:
        # only include rows that are pixel FEDs
        if isPixFED(row):
            output_data.append(row)
    return output_data
#---------------------------------------------------
# Sample JSON data
with open('FEDMonitor_2023_09_01_v2.json', 'r') as json_file:
    raw_data = json.load(json_file)
@app.route('/')
def index():
    headers=raw_data['table']['definition']
    #data=data['table']['rows']
    #moving connectionName dictionary to front
    fed_num = headers.pop(-7)
    headers.insert(0,fed_num)    
    
    return render_template('index_work.html', 
    						fed_data=process_data(raw_data['table']['rows']),
    						headers=raw_data['table']['definition'])

if __name__ == '__main__':
    app.run(debug=True)