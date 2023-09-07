# display_fed_data.py

import tools
import datetime
from flask import Flask, render_template

# TODO
# - Load live FED data in json format using requests library
# - Only put FED status logic in python (not html): save as a new variable
# - Freeze header row so that it is always visible
# - Sort by any column
# - Sort by FED number
# - Customize browser tab icon and name.
# - Add "Refresh" button at the top

# DONE
# - Get FED status based on multiple variables
# - Do not inlucde non-FED rows in FED status counts
# - Do not inlucde non-FED rows html table: remove rows
# - Right justify entries in table
# - Make columns wider in table
# - Change to a better font
# - Make background colors (gray, green, red, etc.) transparent

app = Flask(__name__)

# Display FED data from input json file.

# for a dict in the table, print keys and values
def print_table_dict(input_data, my_key):
    my_dict = input_data["table"][my_key]
    for key, value in my_dict.items(): 
        print("{0}: {1}".format(key, value))

# for a list in the table, print keys and values
def print_table_list(input_data, my_key):
    my_list = input_data["table"][my_key]
    for element in my_list:
        this_key    = element["key"]
        this_type   = element["type"]
        print("{0}: {1}".format(this_key, this_type))

# for rows in the table, print a specific keys and values
def print_table_rows(input_data, my_keys):
    my_rows = input_data["table"]["rows"]
    for row in my_rows:
        message = ""
        for key in my_keys:
            value = row[key]
            # check if message is not empty
            if message:
                message += ", {0}: {1}".format(key, value)
            else:
                message += "{0}: {1}".format(key, value)
        print(message)

# process data
def process_data(input_data):
    output_data = []
    for row in input_data:
        # only include rows that are pixel FEDs
        if isPixFED(row):
            output_data.append(row)
    return output_data

# check if row is a pixel FED based on the board code.
# note: the correct board code is "PIX FED ", including the space at the end.
def isPixFED(row):
    answer = "PIX FED "
    board_code = row["BoardCode"]
    if board_code == answer:
        return True
    else:
        return False

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

# use html template with conditional statements and loops
@app.route('/display_fed_data')
def result():
    # input json file with data
    input_file  = "data/FEDMonitor_2023_09_01_v2.json"
    
    # load data from json file
    raw_data    = tools.load_data(input_file)
    
    # print data
    #print("--------------------")
    #tools.print_key_depth(raw_data)
    #print("--------------------")
    #print_table_dict(raw_data, "properties")
    #print("--------------------")
    #print_table_list(raw_data, "definition")
    #print("--------------------")
    #print_table_rows(raw_data, ["connectionName", "EvtErrNumTot", "RocErrNumTot"])
    #print("--------------------")
    
    # format data
    table_rows = process_data(raw_data["table"]["rows"])
    
    # get counts
    fed_counts = get_counts(table_rows, ["EvtErrNumTot", "RocErrNumTot"])
    
    return render_template('display_fed_data.html', fed_counts=fed_counts, fed_data=table_rows)

if __name__ == '__main__':
    app.run(debug=True)
