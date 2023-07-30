# python-utilities
### Various utilities written in python

The purpose of this repo is to contain various scripts written in python as utilities to solve specific problems.

# Find_Excel_Data_Length - Excel Data Length Finder
This script is used to read an Excel file and find any cells in which the length of the content exceeds a specified maximum length. This can be useful to identify what data is exceeding the max length for a given data store such as SQL Server tables.

## Usage

The script takes two command-line arguments:

1. The path to the Excel file
2. The maximum length for the cell content

You can run the script from the command line as follows:

`python find_excel_data_length.py <file_path> <max_length>`

## Example
`python find_excel_data_length.py /path/to/data.xlsx 50`

The script will output information about any cells in which the length of the content exceeds the maximum length. For each such cell, it will print the column name, the row index, and the cell value.

<br><br>

# Download_Web_Page - Webpage Downloader Script

This script downloads a webpage and its embedded images from a specified URL to a local directory. 

## Usage
To use the script, use the following command:

`python download_webpage.py [url] [local_directory]`

## Options

- `[url]`: The URL of the webpage you wish to download. This must be a valid URL. 
- `[local_directory]`: The path to the local directory where the downloaded webpage and its images will be saved. If the directory does not already exist, it will be created.

## Example

`python download_webpage.py https://www.example.com/path/to/page`

## Notes

- This script uses the `requests` library to send HTTP requests and `BeautifulSoup` from the `bs4` library to parse HTML content.
- It saves the downloaded webpage as `index.html` in the specified local directory.
- Images found on the webpage are also downloaded to the same directory, maintaining their original file names (after sanitizing).
- All download operations are performed using GET requests. If a request fails, an error message is printed to the console.

<br><br>



# PyTree - Directory Listing Script

This script lists directories in a tree-like format starting from a given root directory.

## Usage

To run the script, use the following command:

`python tree.py <startpath> [-e <dir1> <dir2> ...] [-f <true/false>]`

- `<startpath>`: This is the root directory from which to list directories. It's a mandatory argument.

### Options

- `-e, --exclude <dir1> <dir2> ...`: A list of directory names to exclude. Multiple directories can be specified. If not provided, no directories will be excluded.

- `-f, --files <true/false>`: Include files in the output. Set this to "true" or "false". The default is "false", i.e., files are not included in the output.

## Examples

- To list all directories (excluding files) under the current directory:

`python tree.py . -f false`

- To list directories and files under `/usr/local`, excluding the `bin` and `etc` directories:

`python tree.py /usr/local -e bin etc -f true`

## Notes

- The script must be run with Python 3.
- The path provided should be accessible to the script for it to work correctly.
