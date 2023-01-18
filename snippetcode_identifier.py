import requests
from bs4 import BeautifulSoup
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="The hostname of the server to connect to")
parser.add_argument("port", type=int, help="The port number of the server to connect to")
args = parser.parse_args()

# make an HTTP request to the website
response = requests.get(args.hostname)

# create a BeautifulSoup object from the response
soup = BeautifulSoup(response.text, 'html.parser')

# parse the HTML
# ...

# find all code snippets
code_snippets = soup.find_all('script')

# loop through all snippets
for snippet in code_snippets:
  if '_fs_debug' in snippet.text:
    # found the code snippet
    print('Code snippet found!')
else:
     print("Code not found! ")
