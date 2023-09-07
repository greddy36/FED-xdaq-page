from flask import Flask, render_template
import urllib.request
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
# Define the proxy settings with authentication

url = 'http://kvm-s3562-3-ip157-27.cms:9945/urn:xdaq-application:lid=16/retrieveCollection?fmt=json&flash=urn:xdaq-flashlist:FEDMonitor'
with urllib.request.urlopen(url) as json_file:
    raw_data = json.load(json_file)
    print(raw_data)
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