# CSVparse
A tool to parse multiple CSV files into object arrays contained in a single Javascript file.
## Installation
Requires Python 2.7x This should already be installed with ArcGIS. 

### Install the required python libraries
Open the command shell and type:


`pip install -r /path/to/requirements.txt`


where /path/to/requirements.txt is the location of the requirements.txt file. This will be in the same directory as the script.
You may need to provide the full path to pip (.../Python27/ArcGIS10.2/Scripts/pip.exe): 


`/path/to/pip.exe install - r /path/to/requirements.txt`

Once you have installed the requirements, see [Running the script](##running-the-script) below.
See below if you receive an error saying "pip" is not a recognized command or a similar error.

### If pip is not installed
Pip should be installed with Python 2.7.9 and later. If pip is not installed, you will need to install it manually (which 
may need administrator access).

Download [get-pip.py](http://pip.readthedocs.org/en/stable/installing/) (right click, "save link as...") : 

Open the command shell and type:


`python /path/to/get-pip.py`


where /path/to/get-pip.py is the location of the downloaded `get-pip.py` script file.
Note: This assumes that python is correctly added to the PATH system variables on your machine. If not, you will have to supply the full
path to the python executable. 

`/path/to/python.exe /path/to/get-pip.py`

## Running the script
Run the script by opening the command line and typing:

`python /path/to/csvparse.py`

where /path/to/csvparse.py is the full path to the script file. You can alternatively navigate to the directory
containing `csvparse.py` in the command line, and type:

`python csvparse.py`
