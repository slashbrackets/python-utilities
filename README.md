# python-utilities
### Various utilities written in python

The purpose of this repo is to contain various scripts written in python as utilities to solve specific problems.

- **find-excel-data-length.py** - this script will find which column, row, and data in an excel spreadsheet that exceeds the length specified. This is useful to find what data is exceeding the length allowed in a database if performing uploads to SQL or some other strongly typed data store. Usage: `python find-excel-data-length.py <file_path> <max_length>`

- **download_webpage.py** - this script will download a web page based on the URL provided and outputs to a local directory specified. It will include images and sanitize the image names to prevent invalid character names. Usage: `python download_webpage.py <url of webpage> <local directory>`

- **tree.py** - similar to the DOS TREE command this script will draw a directory tree and allows exclusion of specific folders. Usage: `python tree.py /path/to/root -e node_modules other_folder_to_exclude -f true`