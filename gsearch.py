#!/usr/bin/python3
from urllib import parse
from sys import argv


def gsearch_clean_url(input_url_str):
    print('Cleaning URL:\n', input_url_str, '\n')
    # Get starting index of URL: &url=
    url_start = 5 + input_url_str.find('&url=')
    # Get ending index of URL: &usg
    url_end = input_url_str.find('&usg')
    clean_url = parse.unquote_plus(input_url_str[url_start:url_end])
    print('Cleaned url:\n', clean_url)


if __name__ == '__main__':
    input_url_str = str(argv[1])
    gsearch_clean_url(input_url_str)
