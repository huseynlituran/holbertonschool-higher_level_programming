#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    # Firewall təhlükəsizliyini keçmək üçün xüsusi başlıq əlavə edirik
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
