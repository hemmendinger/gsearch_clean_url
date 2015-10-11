#!/usr/bin/python3
from urllib import parse
from sys import argv

input_url_str = str(argv[1])
print('Cleaning URL:\n', input_url_str, '\n')

# Get starting index of URL: &url=
url_start = 5 + input_url_str.find('&url=')
# Get ending index of URL: &usg
url_end = input_url_str.find('&usg')

clean_url = parse.unquote_plus(input_url_str[url_start:url_end])

print('Cleaned url:\n', clean_url)
