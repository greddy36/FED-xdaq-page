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

# get FED status (0: error, 1: ok) based on variables
def getFEDStatus(row, variables):
    for variable in variables:
        value = row[variable]
        if value != 0:
            return 0
    return 1
    
# count number of FEDs in a certain status based on variables
def get_counts(table_rows, variables):
    counts = {}
    
    n_total = 0
    n_ok    = 0
    n_error = 0
    
    for row in table_rows:
        n_total += 1
        # get FED status based on variables
        status = getFEDStatus(row, variables)
        if status:
            n_ok += 1
        else:
            n_error += 1

    counts["n_total"]   = n_total
    counts["n_ok"]      = n_ok
    counts["n_error"]   = n_error
    
    return counts
#---------------------------------------------------
# Sample JSON data
with open('FEDMonitor_2023_09_01_v2.json', 'r') as json_file:
    raw_data = json.load(json_file)
@app.route('/index_work.html')
def index():
    headers=raw_data['table']['definition']
    #data=data['table']['rows']
    #moving connectionName dictionary to front
    fed_num = headers.pop(-7)
    headers.insert(0,fed_num)    
        
    return render_template('index_work.html', 
    						fed_data=process_data(raw_data['table']['rows']),
    						headers=raw_data['table']['definition'])
@app.route('/display_fed_data.html')
def fed_err_data():#for Caleb's error page        
    fed_data=process_data(raw_data['table']['rows'])
    return render_template('display_fed_data.html',
                 fed_counts=get_counts(fed_data, ["EvtErrNumTot", "RocErrNumTot"]),
                 fed_data=fed_data)
			

if __name__ == '__main__':
    app.run(debug=True)