"""
Iterates through each csv file in a location and 
outputs data to data.js as JSON-formatted object array attached 
to a variable (generated from csv file name). 
Note: output is not true JSON.

"""
import os
import csvkit
import json
import chardet
from collections import OrderedDict

CSV_FILE_LOCATION = raw_input("Enter the directory which contains the CSV files for parsing: ")
DATA_OUTPUT = raw_input("Save output to: ")

def file_check(file_path):
	if os.path.exists(file_path):
		overwrite_prompt = raw_input("Output file already exists.Overwrite existing file? Y/N: ")
		if overwrite_prompt.lower() == 'y':
			os.remove(file_path)
		elif overwrite_prompt.lower() == 'n':
			while True:
				new_data_out = raw_input("Enter new output file path: ")
				if os.access(os.path.dirname(new_data_out),os.W_OK) and os.path.abspath(new_data_out) != os.path.abspath(file_path):
					file_path = os.path.abspath(new_data_out)
					break 
				else:
					print "Invalid directory path. Please enter the full path for the new output file."
		else:
			print "Did not recognize input. Please enter 'Y' or 'N'"
	if os.path.splitext(file_path)[1] != '.js':
		file_path = os.path.splitext(file_path)[0] + '.js'
	return file_path	
		

def csv_parse(file_location,output):
	for filename in os.listdir(file_location):
		if not filename.endswith('.csv'):
			continue
		csv_rows = []
		obj_list = []
		name = os.path.splitext(os.path.basename(filename))[0]
		file = os.path.join(file_location,filename)
		print "Parsing file: ",file
		
		with open(file,'rb') as csv_file:
			raw_data = csv_file.read()
			detected = chardet.detect(raw_data)
			codec = detected['encoding']
			confidence = detected['confidence']
			print "Detected file encoding: ",codec
			print "Confidence: ",confidence
		with open(file,'rb') as csv_file:
			csv_reader = csvkit.py2.CSVKitReader(csv_file,encoding = codec)
			for row in csv_reader:
				csv_rows.append(row)
		headers = [header for header in csv_rows[0]]
		for row in csv_rows:
			if row == csv_rows[0]:
				continue
			obj = OrderedDict()
			for i in range(len(headers)):
				obj[headers[i]] = row[i]
			obj_list.append(obj) 
		
		with open(output,'ab') as js_file:
			js_file.write('var {0} = '.format(name))
			json.dump(obj_list,js_file)
			js_file.write('\n\n')		
		print "Done."
	print "Finished parsing all files."
		

if __name__ == '__main__':
	csv_parse(CSV_FILE_LOCATION,file_check(DATA_OUTPUT))

	