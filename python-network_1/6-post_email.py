#!/usr/bin/python3
"""
A script that takes in email address, sends a POST request to the
passed URL with the ema, and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # POST sorğusu üçün məlumatı lüğət kimi hazırlayırıq
    payload = {'email': email}
    # requests.post metodu avtomatik olaraq məlumatı emal edir
    r = requests.post(url, data=payload)
    print(r.text)
