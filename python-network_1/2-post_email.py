#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Göndəriləcək məlumatı lüğət (dictionary) kimi hazırlayırıq
    values = {'email': email}

    # Məlumatı URL parametrləri formatına (key=value) salırıq
    data = urllib.parse.urlencode(values)

    # Məlumatı bayt (bytes) formatına çeviririk (POST data üçün mütləqdir)
    data = data.encode('ascii')

    # Request obyektini yaradarkən 'data' parametrini ötürürük.
    # Bu, sorğunun avtomatik olaraq POST olmasını təmin edir.
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        # Cavabı oxuyuruq və utf-8 ilə dekod edirik
        print(response.read().decode('utf-8'))
